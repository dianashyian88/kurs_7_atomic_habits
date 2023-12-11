from celery import shared_task
from users.models import User
from habits.models import Habit
from habits.services import MyBot
import datetime
from django.utils import timezone


@shared_task
def check_user_habit():
    list_user = User.objects.all()
    for obj in list_user:
        if not obj.telegram_id:
            return False
        now = datetime.datetime.now()
        now = timezone.make_aware(now, timezone.get_current_timezone())
        now_time = datetime.timedelta(hours=now.hour,
                                      minutes=now.minute,
                                      seconds=now.second)
        list_habit = Habit.objects.filter(owner=obj.id,
                                          is_enjoy_habit=False)
        for habit in list_habit:
            my_bot = MyBot()
            text = f'Я буду {habit.action} в {habit.time} в {habit.place}'
            chat_id = obj.telegram_id
            habit_time = datetime.timedelta(hours=habit.time.hour,
                                            minutes=habit.time.minute,
                                            seconds=habit.time.second)
            time_delta = (habit_time - now_time).total_seconds() / 3600
            if habit.last_reminder is not None:
                day_delta = (now - habit.last_reminder).total_seconds()
            else:
                day_delta = (now - habit.create_date).total_seconds()
            if habit.periodicity == 'once_day':
                my_bot.once_day_send_message(habit, day_delta, time_delta, now, text, chat_id)
            elif habit.periodicity == 'once_week':
                my_bot.once_week_send_message(habit, day_delta, time_delta, now, text, chat_id)
            elif habit.periodicity == 'twice_week':
                my_bot.twice_week_send_message(habit, day_delta, time_delta, now, text, chat_id)
