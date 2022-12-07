from django.urls import path

from comments.views import CommentViewSet

urlpatterns = [
    path('<int:comment_id>', CommentViewSet.as_view(actions={
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
