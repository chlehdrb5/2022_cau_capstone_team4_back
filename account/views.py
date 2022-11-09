from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from .models import User
from rest_framework import generics

# Create your views here.


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        user = serializer.instance
        token = Token.objects.create(user=user)
        return Response({"Token": token.key})


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        print(request.data)
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status=401)
