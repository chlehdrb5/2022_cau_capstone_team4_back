from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.name')
    # post = serializers.ReadOnlyField(source='post.id')
    # answer = serializers.ReadOnlyField(source='answer.id')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'answer', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ('answer', 'post', 'author')
