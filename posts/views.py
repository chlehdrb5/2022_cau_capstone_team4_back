from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from paint_int_prj.constant import *
from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer
from rest_framework import viewsets, status


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'

    def get_queryset(self):
        if 'username' in self.kwargs:
            username = self.kwargs['username']
            return Post.objects.filter(author__username=username)
        else:
            return Post.objects.all()

    def create(self, request, *args, **kwargs):
        if 'point' not in request.data or not request.data['point']:
            post_point = DEFAULT_POST_POINT
        else:
            post_point = request.data['point']
        if post_point > self.request.user.point:
            return Response({"Error": "포인트가 부족합니다."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        self.request.user.point -= post_point
        self.request.user.save()

        new_data = dict(serializer.data)
        post = Post.objects.get(id=serializer.data['id'])
        post.thumbnail = post.file_upload
        post.save()
        new_data['thumbnail'] = post.thumbnail
        return Response(new_data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if post.answer_set:
            return Response({"Error": "답변이 작성된 게시글은 삭제할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if post.answer_set:
            return Response({"Error": "답변이 작성된 게시글은 수정할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
