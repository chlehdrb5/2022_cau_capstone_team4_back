from rest_framework import serializers

from paint_int_prj.constant import *
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.name')
    # post = serializers.ReadOnlyField(source='post.id')
    is_liked = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    def get_is_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated and obj.like_users.filter(pk=request.user.pk).exists():
            return True
        return False

    def get_like_count(self, obj):
        return obj.like_users.count()

    class Meta:
        model = Answer
        fields = ('id', 'post', 'file_upload', 'author', 'created_at',
                  'updated_at', 'selected', 'savedata', 'is_liked', 'like_count')
        read_only_fields = ('selected', 'post', 'author')
