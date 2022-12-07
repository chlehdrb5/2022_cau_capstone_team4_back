from rest_framework import serializers
from .models import Post, Tag


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    cumul_point = serializers.SerializerMethodField()

    def get_cumul_point(self, obj):
        return obj.author.cumul_point

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'tag', 'file_upload',
                  'author', 'created_at', 'updated_at', 'selected', 'point', 'thumbnail', 'cumul_point')
        read_only_fields = ('selected', 'thumbnail', 'author', 'cumul_point')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )

