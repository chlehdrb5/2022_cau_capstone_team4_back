from rest_framework import serializers
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    # like_count = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ('id', 'post', 'content', 'head_image', 'file_upload', 'author', 'created_at', 'updated_at', 'selected', 'like_users')

    # def get_like_count(self, obj):
    #     return obj.like_users.count
