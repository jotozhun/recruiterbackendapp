from core.models import User
from core.serializers import UserSerializer, RegisterSerializer, LoginUserSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from core.encryption import TokenEncrypter

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class RegisterAPI(generics.GenericAPIView):
    """
    Register View
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """Crate a user"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user is not None:
            try:
                token = Token.objects.get(user_id=user.id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            token_encrypted = TokenEncrypter().encrypt_user_token(token.key, ttl=0)
            return Response({"token": token_encrypted}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response([], status=status.HTTP_401_UNAUTHORIZED)
        # return Response({
        #     "user": UserSerializer(user, context=self.get_serializer_context()).data,
        #     "token": AuthToken.objects.create(user)[1]
        # })
