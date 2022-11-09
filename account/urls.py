from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', views.SignupView.as_view()),
    path('login/', views.LoginView.as_view()),
]
