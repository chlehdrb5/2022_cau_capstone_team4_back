from django.db.models import Count
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.viewsets import ModelViewSet

from paint_int_prj.constant import *
from posts.models import Post
from .serializers import AnswerSerializer
from .models import Answer
# Create your views here.


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_url_kwarg = 'answer_id'

    def get_queryset(self):
        if 'username' in self.kwargs:
            username = self.kwargs['username']
            return Answer.objects.filter(author__username=username)
        if 'post_id' in self.kwargs:
            post_id = self.kwargs['post_id']
            return Answer.objects.filter(post_id=post_id)
        else:
            return Answer.objects.all()

    def create(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs['post_id'])
        # print(f"Test : {post}")
        if post.selected == FINAL_SELECTED:
            return Response({"Error": "최종 채택이 완료된 게시글에는 답변을 작성할 수 없습니다.."}, status=status.HTTP_400_BAD_REQUEST)
        elif post.selected == MID_SELECTED:
            mid_selected_answer = post.answer_set.filter(selected=MID_SELECTED)[0]
            if request.user != mid_selected_answer.author:
                return Response({"Error": "중간 채택된 답변의 작성자만 답변을 작성할 수 있습니다."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        self.request.user.point += ANSWER_POINT
        self.request.user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        if 'post_id' in self.kwargs:
            post_id = self.kwargs['post_id']
            post = Post.objects.get(id=post_id)
            serializer.save(post=post)
            if post.selected == MID_SELECTED:
                serializer.save(selected=MID_SELECTED)

    def like(self, request, *args, **kwargs):
        answer = self.get_object()
        if request.user.is_authenticated:
            # if request.user.is_authenticated # 현재 로그인 한 사용자만 like 사용가능하도록 setting되어있음

            if answer.like_users.filter(pk=request.user.pk).exists():
                # 이미 해당 answer에 좋아요를 누른 경우
                answer.like_users.remove(request.user)
            else:
                # 좋아요를 누르면 추가
                answer.like_users.add(request.user)
            answer.save()

        return Response({"like_count": answer.like_users.count()})

    def select(self, request, *args, **kwargs):
        answer = self.get_object()
        post = answer.post
        # print(post)
        # print(post.answer_set.all())
        if request.user.is_authenticated and request.user == post.author:
            # print(post.answers)
            if post.selected == FINAL_SELECTED:
                return Response({"Error": "이미 채택이 완료된 게시글입니다."}, status=status.HTTP_400_BAD_REQUEST)
            elif post.selected == MID_SELECTED:     # 최종 채택을 하는 경우
                mid_selected_answer = post.answer_set.filter(selected=MID_SELECTED)[0]
                if answer.author != mid_selected_answer.author:
                    return Response({"Error": "중간 채택된 답변의 작성자와 일치하지 않는 답변입니다."}, status=status.HTTP_400_BAD_REQUEST)
                answer.selected = FINAL_SELECTED
                post.selected = FINAL_SELECTED
            elif post.selected == NOT_SELECTED:     # 중간 채택 하는 경우
                answer.selected = MID_SELECTED
                post.selected = MID_SELECTED
            answer.author.point += post.point // 2
            answer.author.save()
            answer.save()
            post.thumbnail = answer.file_upload
            post.save()

            return Response({"selected": answer.selected})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class AnswerRankViewSet(ModelViewSet):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.all().annotate(like_cnt=Count('like_users')).order_by('-like_cnt')[:9]
