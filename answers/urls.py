from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from comments.views import AnswerCommentViewSet
from .views import AnswerViewSet

urlpatterns = [
    path('', AnswerViewSet.as_view(actions={
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', AnswerViewSet.as_view(actions={
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('<int:pk>/like/', AnswerViewSet.as_view(actions={
        'get': 'like',
    })),
    path('<int:answer_pk>/comment/', AnswerCommentViewSet.as_view(actions={
        'get': 'list',
        'post': 'create'
    })),
    path('<int:answer_pk>/comment/<int:comment_pk>/', AnswerCommentViewSet.as_view(actions={
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
