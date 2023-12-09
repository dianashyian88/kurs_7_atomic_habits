from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import RegistrationSerializer, LoginSerializer
from rest_framework import generics


class RegistrationAPIView(generics.CreateAPIView):
    """Эндпойнт регистрации пользователя"""
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class LoginAPIView(APIView):
    """Эндпойнт авторизации пользователя"""
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
