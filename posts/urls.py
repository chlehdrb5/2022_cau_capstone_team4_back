from django.urls import path
from .views import PostViewSet

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('post/', post_list),
    path('post/<int:pk>/', post_detail),
]

'''
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostList, PostDetail

urlpatterns = [
    path('post/', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
'''
