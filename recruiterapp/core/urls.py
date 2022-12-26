from .views import RegisterAPI, UserAPI, VerifyEmail, LoginAPI
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserAPI.as_view(), name='user'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify")
]
