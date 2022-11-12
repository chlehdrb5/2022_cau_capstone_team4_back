from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from comments.views import CommentViewSet
from .views import AnswerViewSet

urlpatterns = [
    path('', AnswerViewSet.as_view(actions={
        'get': 'list',
    })),
    path('<int:answer_id>', AnswerViewSet.as_view(actions={
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('<int:answer_id>/like', AnswerViewSet.as_view(actions={
        'get': 'like',
    })),
    path('<int:answer_id>/comments', CommentViewSet.as_view(actions={
        'get': 'list',
        'post': 'create'
    })),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
