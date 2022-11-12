from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.viewsets import ModelViewSet

from .serializers import AnswerSerializer
from .models import Answer
# Create your views here.


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_url_kwarg = 'answer_id'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        serializer_data_ = dict(serializer.data)
        serializer_data_["is_liked"] = False
        answer = self.get_object()
        if request.user.is_authenticated:
            if answer.like_users.filter(pk=request.user.pk).exists():
                serializer_data_["is_liked"] = True
        print(serializer_data_)
        return Response(serializer_data_)

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
        