from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Модель пользователей"""
    username = models.CharField(max_length=100, verbose_name='ФИО', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=40, verbose_name='номер телефона', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    email_verify = models.BooleanField(default=False)
    telegram_id = models.PositiveIntegerField(verbose_name='user_id в Telegram', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
