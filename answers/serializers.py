from rest_framework import serializers
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Answer
        fields = ('id', 'post', 'content', 'author', 'created_at', 'updated_at', 'selected')
