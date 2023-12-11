from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_register_user(self):
        """Тестирование регистрации пользователя"""

        User.objects.create(
            id=1,
            email="user1@user.user",
            password="qweasdzxc"
        )

        data = {
                   "username": "user1",
                   "email": "user1111111@user.user",
                   "password": "qweasdzxc"
        }

        response = self.client.post(
            '/users/registration/',
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
