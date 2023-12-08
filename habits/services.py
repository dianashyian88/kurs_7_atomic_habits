from django.conf import settings
import requests


class MyBot:
    URL = settings.TELEGRAM_URL
    TOKEN = settings.TELEGRAM_TOKEN

    def send_message(self, text, chat_id):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
