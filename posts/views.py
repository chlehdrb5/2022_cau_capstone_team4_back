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
        if 'user_id' in self.kwargs:
            user_id = self.kwargs['user_id']
            return Post.objects.filter(author=user_id)
        else:
            return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


'''
class TagList(APIView):
    def get_object(self, slug):
        try:
            return Tag.objects.get(slug=slug)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        tag = self.get_object(slug)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
'''

'''
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)

    serializer = TagSerializer(tag, many=True)
    return Response(serializer.data)
'''


'''
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import PostSerializer
from .models import Post

# Create your views here.

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''