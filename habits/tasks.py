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
        if obj.telegram_id is not None:
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
                    if day_delta / 60 > 60:
                        if 0 < time_delta < 1:
                            my_bot.send_message(text, chat_id)
                            habit.last_reminder = now
                            habit.save()
                elif habit.periodicity == 'once_week':
                    if 6 < day_delta / 3600 < 7:
                        if 0 < time_delta < 1:
                            my_bot.send_message(text, chat_id)
                            habit.last_reminder = now
                            habit.save()
                elif habit.periodicity == 'twice_week':
                    if 1 < day_delta / 3600 < 2:
                        if 0 < time_delta < 1:
                            my_bot.send_message(text, chat_id)
                            habit.last_reminder = now
                            habit.save()
