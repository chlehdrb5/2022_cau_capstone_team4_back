from django.urls import path

from comments.views import CommentViewSet

urlpatterns = [
    path('', CommentViewSet.as_view(actions={
        'get': 'list',
    })),
]
