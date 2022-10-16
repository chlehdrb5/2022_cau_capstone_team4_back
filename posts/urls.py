from django.urls import path

from .views import PostViewSet, TagViewSet

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

tag_list = TagViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('', post_list),
    path('<int:pk>/', post_detail),
    path('tag/', tag_list),
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
