import jwt

from core.models import User
from core.serializers import UserSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from datetime import datetime

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class RegisterAPI(generics.GenericAPIView):
    """
    Register View
    """
    # permission_classes = [permissions.AllowAny, ]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """Create a user"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.email+' Use linkn below to verify your email\n'+absurl
        data={'email_body': email_body, 'to_email': user.email,'email_subject': 'Verify your email'}
        Util.send_email(data)
        
        return Response({
            "user": UserSerializer(user_data, context=self.get_serializer_context()).data,
        })

class LoginAPI(TokenObtainPairView):
    """Hello"""
    
    def post(self, request, *args, **kwargs):
        data = super().post(request, args, kwargs).data
        try:
            payload = jwt.decode(data["access"], settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            user.last_login = datetime.now()
            user.save()
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'error': "An Unexpected error has occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VerifyEmail(generics.GenericAPIView):

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({
                'email': "Successfully activated"},
                status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as expired_error:
            return Response({
                'error': "Activation Expired"},
                status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as decode_error:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
