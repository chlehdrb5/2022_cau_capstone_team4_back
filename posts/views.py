from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer
from rest_framework import viewsets


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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
