from .models import User
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.ManyRelatedField

    class Meta:
        model = User
        fields = ['username', 'email', 'point', ]


class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
