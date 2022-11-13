from django.urls import path, include

from answers.views import AnswerViewSet
from comments.views import CommentViewSet
from .views import UserViewSet, SignupView, SigninView
from posts.views import PostViewSet
from rest_framework import urls

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('',        UserViewSet.as_view(actions={         # users
        'get': 'list',
    })),

    # user/
    path('signup', SignupView.as_view()),
    path('signin', SigninView.as_view()),
    # path('signout', views.SignoutView.as_view()),
    path('<str:username>', UserViewSet.as_view(actions={
        'put': 'update',
        'get': 'retrieve',
    })),
    path('<str:username>/posts', PostViewSet.as_view(actions={
        'get': 'list',
    })),
    path('<str:username>/answers', AnswerViewSet.as_view(actions={
        'get': 'list',
    })),
    path('<str:username>/comments', CommentViewSet.as_view(actions={
        'get': 'list',
    })),
    path('<str:username>/post/<int:post_id>/comments', CommentViewSet.as_view(actions={
        'get': 'list',
    })),
    path('<str:username>/answer/<int:answer_id>/comments', CommentViewSet.as_view(actions={
        'get': 'list',
    }))
]
