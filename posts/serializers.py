from rest_framework import serializers
from .models import Post, Tag


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'tag', 'file_upload',
                  'author', 'created_at', 'updated_at', 'selected', 'point')
        read_only_fields = ('selected',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )

