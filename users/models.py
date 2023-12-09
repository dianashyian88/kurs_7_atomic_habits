from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
import jwt
from django.conf import settings


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Модель пользователей"""
    username = models.CharField(max_length=100,
                                verbose_name='ФИО',
                                **NULLABLE)
    email = models.EmailField(unique=True,
                              verbose_name='почта')
    phone = models.CharField(max_length=40,
                             verbose_name='номер телефона',
                             **NULLABLE)
    city = models.CharField(max_length=50,
                            verbose_name='город',
                            **NULLABLE)
    avatar = models.ImageField(upload_to='users/',
                               verbose_name='аватар',
                               **NULLABLE)
    email_verify = models.BooleanField(default=False)
    telegram_id = models.PositiveIntegerField(
        verbose_name='user_id в Telegram',
        **NULLABLE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.email

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token, вместо
        user._generate_jwt_token().
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать username.
        """
        return self.username

    def get_short_name(self):
        """ Аналогично методу get_full_name(). """
        return self.username

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
