from rest_framework.serializers import ValidationError
from habits.models import Habit


class TimeHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None and tmp_val > 120:
            raise ValidationError('Временной отрезок не может '
                                  'превышать 120 секунд. '
                                  'В поле time_habit введите '
                                  'значение от 0 до 120 ')


class LinkHabitHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        queryset = Habit.objects.filter(is_enjoy_habit=True)
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None and tmp_val not in queryset:
            raise ValidationError('В связанные привычки '
                                  'могут попадать только '
                                  'привычки с признаком '
                                  'приятной привычки')
