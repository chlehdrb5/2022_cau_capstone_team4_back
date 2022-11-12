from django.urls import path

from comments.views import CommentViewSet

urlpatterns = [
    path('', CommentViewSet.as_view(actions={
        'get': 'list',
    })),
    path('<int:comment_id>', CommentViewSet.as_view(actions={
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
