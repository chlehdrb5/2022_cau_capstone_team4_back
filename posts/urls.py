from django.urls import path


from comments.views import CommentViewSet
from answers.views import AnswerViewSet
from .views import PostViewSet, TagViewSet


urlpatterns = [
    path('', PostViewSet.as_view(actions={
        'get': 'list',
        'post': 'create'
    })),
    path('<int:post_id>', PostViewSet.as_view(actions={
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('<int:post_id>/answers', AnswerViewSet.as_view(actions={
        'post': 'create',
    })),
    path('<int:post_id>/comments', CommentViewSet.as_view(actions={
        'get': 'list',
        'post': 'create',
    })),
    path('tag/', TagViewSet.as_view(actions={
        'get': 'list',
    })),
]

'''
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
'''
