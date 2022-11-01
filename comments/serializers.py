from rest_framework import serializers
from .models import Comment, AnswerComment, PostComment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'created_at', 'updated_at']


class PostCommentSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = PostComment
        fields = ['id', 'post', 'content', 'author', 'created_at', 'updated_at']


class AnswerCommentSerializer(CommentSerializer):
    answer = serializers.ReadOnlyField(source='answer.id')
    # post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = AnswerComment
        fields = ['id', 'answer', 'content', 'author', 'created_at', 'updated_at']
