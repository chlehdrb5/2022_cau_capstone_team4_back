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
    lookup_url_kwarg = 'comment_id'

    def get_queryset(self):
        if 'username' in self.kwargs:
            username = self.kwargs['username']
            if 'answer_id' in self.kwargs:
                answer_id = self.kwargs['answer_id']
                return Comment.objects.filter(answer_id=answer_id, author__username=username)
            if 'post_id' in self.kwargs:
                post_id = self.kwargs['post_id']
                return Comment.objects.filter(post_id=post_id, author__username=username)
            return Comment.objects.filter(author__username=username)
        if 'answer_id' in self.kwargs:
            answer_id = self.kwargs['answer_id']
            return Comment.objects.filter(answer_id=answer_id)
        if 'post_id' in self.kwargs:
            post_id = self.kwargs['post_id']
            return Comment.objects.filter(post_id=post_id)
        else:
            return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        if 'post_id' in self.kwargs:
            post_id = self.kwargs['post_id']
            post = Post.objects.get(id=post_id)
            serializer.save(post=post)
        if 'answer_id' in self.kwargs:
            answer_id = self.kwargs['answer_id']
            answer = Answer.objects.get(id=answer_id)
            serializer.save(answer=answer)
            # serializer.save(post=answer.post)

    def get_object(self):
        if self.action == 'list':
            super().get_object()
        if self.action in ['retrieve', 'update', 'destroy']:
            comment_id = self.kwargs['comment_id']
            obj = Comment.objects.get(id=comment_id)
            return obj
