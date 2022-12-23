from .views import RegisterAPI, LoginAPI, UserAPI
from django.urls import path, include

urlpatterns = [
    path('user/', UserAPI.as_view(), name='user'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
]
