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
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
