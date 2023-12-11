from django.conf import settings
import requests


class MyBot:
    URL = settings.TELEGRAM_URL
    TOKEN = settings.TELEGRAM_TOKEN

    def send_message(self, text, chat_id):
        """Отправляет сообщения в ТГ"""
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )

    def once_day_send_message(self, habit, day_delta, time_delta, now, text, chat_id):
        """Отправляет сообщения в ТГ по привычкам с периодичностью раз в день"""
        if day_delta / 60 > 60:
            if 0 < time_delta < 1:
                self.send_message(text, chat_id)
                habit.last_reminder = now
                habit.save()

    def once_week_send_message(self, habit, day_delta, time_delta, now, text, chat_id):
        """Отправляет сообщения в ТГ по привычкам с периодичностью раз в неделю"""
        if 6 < day_delta / 3600 < 7:
            if 0 < time_delta < 1:
                self.send_message(text, chat_id)
                habit.last_reminder = now
                habit.save()

    def twice_week_send_message(self, habit, day_delta, time_delta, now, text, chat_id):
        """Отправляет сообщения в ТГ по привычкам с периодичностью 2 раза в неделю"""
        if 1 < day_delta / 3600 < 2:
            if 0 < time_delta < 1:
                self.send_message(text, chat_id)
                habit.last_reminder = now
                habit.save()
