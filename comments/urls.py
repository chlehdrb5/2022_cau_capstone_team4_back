from django.urls import path

from comments.views import CommentViewSet, AnswerCommentViewSet, PostCommentViewSet

urlpatterns = [
    path('', CommentViewSet.as_view(actions={
        'get': 'list',
    })),
    path('answer/', AnswerCommentViewSet.as_view(actions={
        'get': 'list',
    })),
    path('post/', PostCommentViewSet.as_view(actions={
        'get': 'list',
    })),
]
