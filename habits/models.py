from django.db import models
from config.settings import AUTH_USER_MODEL
from users.models import NULLABLE


class Reward(models.Model):
    """Модель вознаграждений"""
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)
    action = models.CharField(max_length=100, verbose_name='действие')
    time_habit = models.PositiveSmallIntegerField(verbose_name='время на получение вознаграждения, сек.', **NULLABLE)

    def __str__(self):
        return f'{self.action}, {self.owner}'

    class Meta:
        verbose_name = 'вознаграждение'
        verbose_name_plural = 'вознаграждения'
        ordering = ('id',)


class Habit(models.Model):
    """Модель привычек (в т.ч. полезных и приятных)"""
    PERIODICITY_CHOICES = [
        ('once_2_hours', '1 раз в 2 часа'),
        ('three_times_day', '3 раза в день'),
        ('once_day', '1 раз в день'),
        ('twice_week', '2 раза в неделю'),
        ('once_week', '1 раз в неделю'),
    ]
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_enjoy_habit = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    link_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.CharField(max_length=25, choices=PERIODICITY_CHOICES,
                                   default='once_day', verbose_name='периодичность')
    reward = models.ForeignKey(Reward, on_delete=models.SET_NULL, verbose_name='вознаграждение', **NULLABLE)
    time_habit = models.PositiveSmallIntegerField(verbose_name='время на выполнение привычки, сек.', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='признак публичной привычки')

    def __str__(self):
        return f'{self.action}, {self.periodicity}, {self.owner}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('id',)
