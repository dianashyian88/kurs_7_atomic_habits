from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя и создания нового. """
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'phone', 'city', 'telegram_id', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    """ Сериализация авторизации пользователя по email и паролю"""
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=100, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'Для входа в систему введите email'
            )
        if password is None:
            raise serializers.ValidationError(
                'Для входа в систему введите пароль'
            )
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'Пользователь с таким адресом электронной почты и паролем не найден'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'Данный пользователь неактивен'
            )
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }
