from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer
from rest_framework import viewsets, filters


class MainPageViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().order_by('-updated_at')[:3]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #lookup_field = 'pk'
    lookup_url_kwarg = 'post_id'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']  # 검색 가능 필드
    ordering_fields = ['created_at']  # 정렬 가능 필드
    ordering = ['-updated_at']  # default 정렬 지정

    def get_queryset(self):
        if 'username' in self.kwargs:
            username = self.kwargs['username']
            return Post.objects.filter(author__username=username)
        else:
            return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
