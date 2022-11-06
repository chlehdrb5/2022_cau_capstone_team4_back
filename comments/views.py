from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from answers.models import Answer
from comments.models import Comment
from comments.serializers import CommentSerializer
from posts.models import Post


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        if 'answer_pk' in self.kwargs:
            answer_pk = self.kwargs['answer_pk']
            return Comment.objects.filter(answer_id=answer_pk)
        if 'post_pk' in self.kwargs:
            post_pk = self.kwargs['post_pk']
            return Comment.objects.filter(post_id=post_pk)
        else:
            return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        if 'post_pk' in self.kwargs:
            post_pk = self.kwargs['post_pk']
            post = Post.objects.get(id=post_pk)
            serializer.save(post=post)
        if 'answer_pk' in self.kwargs:
            answer_pk = self.kwargs['answer_pk']
            answer = Answer.objects.get(id=answer_pk)
            serializer.save(answer=answer)

    def get_object(self):
        if self.action == 'list':
            super().get_object()
        if self.action in ['retrieve', 'update', 'destroy']:
            comment_pk = self.kwargs['comment_pk']
            obj = Comment.objects.get(id=comment_pk)
            return obj
