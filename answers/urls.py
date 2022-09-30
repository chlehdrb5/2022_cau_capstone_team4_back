from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AnswerList, AnswerDetail

urlpatterns = [
    path('answer/', AnswerList.as_view()),
    path('answer/<int:pk>/', AnswerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
