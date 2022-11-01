from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from answers.models import Answer
from comments.models import Comment, AnswerComment, PostComment
from comments.serializers import CommentSerializer, AnswerCommentSerializer, PostCommentSerializer
from posts.models import Post


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostCommentViewSet(CommentViewSet):
    # queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

    def get_queryset(self):
        if 'post_pk' in self.kwargs:
            post_pk = self.kwargs['post_pk']
            return PostComment.objects.filter(post_id=post_pk)
        else:
            return PostComment.objects.all()

    def perform_create(self, serializer):
        post_pk = self.kwargs['post_pk']
        post = Post.objects.get(id=post_pk)
        serializer.save(author=self.request.user)
        serializer.save(post=post)

    def get_object(self):
        if self.action == 'list':
            super().get_object()
        if self.action in ['retrieve', 'update', 'destroy']:
            comment_pk = self.kwargs['comment_pk']
            obj = PostComment.objects.get(id=comment_pk)
            return obj


class AnswerCommentViewSet(CommentViewSet):
    # queryset = AnswerComment.objects.all()
    serializer_class = AnswerCommentSerializer

    def get_queryset(self):
        if 'answer_pk' in self.kwargs:
            answer_pk = self.kwargs['answer_pk']
            return AnswerComment.objects.filter(answer_id=answer_pk)
        else:
            return AnswerComment.objects.all()

    def perform_create(self, serializer):
        answer_pk = self.kwargs['answer_pk']
        answer = Answer.objects.get(id=answer_pk)
        serializer.save(author=self.request.user)
        serializer.save(answer=answer)
        # serializer.save(post=answer.post)

    def get_object(self):
        if self.action == 'list':
            super().get_object()
        if self.action in ['retrieve', 'update', 'destroy']:
            comment_pk = self.kwargs['comment_pk']
            obj = AnswerComment.objects.get(id=comment_pk)
            return obj
