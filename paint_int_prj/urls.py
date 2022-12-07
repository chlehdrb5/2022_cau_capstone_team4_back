"""paint_int_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from account.views import UserViewSet
from answers.views import AnswerViewSet
from comments.views import CommentViewSet
from posts.views import PostViewSet, MainPageViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('answer/', include('answers.urls')),
    path('post/', include('posts.urls')),
    path('comment/', include('comments.urls')),
    path('main', MainPageViewSet.as_view(actions={
        'get': 'list',
    })),
    path('users', UserViewSet.as_view(actions={
        'get': 'list',
    })),
    path('posts', PostViewSet.as_view(actions={
        'get': 'list',
        'post': 'create'
    })),
    path('comments', CommentViewSet.as_view(actions={
        'get': 'list',
    })),
    path('answers', AnswerViewSet.as_view(actions={
        'get': 'list',
    })),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)