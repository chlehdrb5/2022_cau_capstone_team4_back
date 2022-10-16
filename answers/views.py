from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.viewsets import ModelViewSet

from .serializers import AnswerSerializer
from .models import Answer
# Create your views here.


# class AnswerList(APIView):
#     def get(self, request): # 답변 보여줄 때
#         answers = Answer.objects.all()
#
#         serializer = AnswerSerializer(answers, many=True)
#         return Response(serializer.data)
#
#     def post(self, request): # 답변 작성 시
#         serializer = AnswerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class AnswerDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Answer.objects.get(pk=pk)
#         except Answer.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         answer = self.get_object(pk)
#         serializer = AnswerSerializer(answer)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         answer = self.get_object(pk)
#         serializer = AnswerSerializer(answer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         answer = self.get_object(pk)
#         answer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def like(self, request, *args, **kwargs):
        answer = self.get_object()
        if request.user.is_authenticated:
            # if request.user.is_authenticated # 현재 로그인 한 사용자만 like 사용가능하도록 setting되어있음

            if answer.like_users.filter(pk=request.user.pk).exists():
                # 이미 해당 answer에 좋아요를 누른 경우
                answer.like_users.remove(request.user)
            else:
                # 좋아요를 누르면 추가
                answer.like_users.add(request.user)
            answer.save()

        return Response({"like_count": answer.like_users.count()})
        