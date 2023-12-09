from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User
from habits.models import Habit, Reward


class RewardTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='Тестов Тест Тестович',
                                             email='test3@mail.ru',
                                             password='123456qwerty')
        self.client.force_authenticate(user=self.user)

    def test_create_reward(self):
        """Тестирование создания вознаграждения"""

        data = {
            "action": "Есть шоколадку",
            "time_habit": "100"
        }
        response = self.client.post(
            '/reward/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "action": "Есть шоколадку",
                "time_habit": 100,
                "owner": 8
            }
        )

        self.assertTrue(
            Reward.objects.all().exists()
        )

    def test_destroy_reward(self):
        """Тестирование удаления вознаграждения"""

        Reward.objects.create(
            id=1,
            action="Есть шоколадку",
            time_habit=100,
            owner=self.user
        )

        response = self.client.delete(
            '/reward/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_list_reward(self):
        """Тестирование выведения списка вознаграждений"""

        Reward.objects.create(
            id=1,
            action="Есть шоколадку",
            time_habit=100,
            owner=self.user
        )

        response = self.client.get(
            '/reward/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results':
                [
                    {
                        "id": 1,
                        "action": "Есть шоколадку",
                        "time_habit": 100,
                        "owner": 10
                    }
                ]
             }
        )

    def test_retrieve_reward(self):
        """Тестирование выведения информации о вознаграждении"""

        Reward.objects.create(
            id=1,
            action="Есть шоколадку",
            time_habit=100,
            owner=self.user
        )

        response = self.client.get(
            '/reward/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "action": "Есть шоколадку",
                "time_habit": 100,
                "owner": 11
            }
        )

    def test_update_reward(self):
        """Тестирование обновления информации о вознаграждении"""

        Reward.objects.create(
            id=1,
            action="Есть шоколадку",
            time_habit=100,
            owner=self.user
        )

        data = {
            "action": "Есть шоколадку и пить кофе",
            "time_habit": "120"
        }

        response = self.client.put(
            '/reward/1/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "action": "Есть шоколадку и пить кофе",
                "time_habit": 120,
                "owner": 12
            }
        )


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='Тестов Тест Тестович',
                                             email='test3@mail.ru',
                                             password='123456qwerty')
        self.client.force_authenticate(user=self.user)

    def test_create_enjoy_habit(self):
        """Тестирование создания приятной привычки"""

        data = {
                    "place": "Любое место в квартире",
                    "time": "10:30:00",
                    "action": "Потискать кота",
                    "periodicity": "once_day",
                    "is_enjoy_habit": "True",
                    "time_habit": "60",
                    "is_public": "True"
        }
        response = self.client.post(
            '/habit/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_habit_with_reward(self):
        """Тестирование создания привычки со ссылкой на вознаграждение"""

        Reward.objects.create(
            id=1,
            action="Есть шоколадку",
            time_habit=100,
            owner=self.user
        )

        data = {
            "place": "Любое место в квартире",
            "time": "10:30:00",
            "action": "Есть фрукты",
            "periodicity": "once_day",
            "is_enjoy_habit": "False",
            "time_habit": "120",
            "reward": 1,
            "is_public": "True"
        }
        response = self.client.post(
            '/habit/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_habit_with_habit(self):
        """Тестирование создания привычки со ссылкой на привычку"""

        Habit.objects.create(
            id=1,
            place="Любое место в квартире",
            time="10:30:00",
            action="Потискать кота",
            periodicity="once_day",
            is_enjoy_habit="True",
            time_habit="60",
            is_public="True",
            owner=self.user
        )

        data = {
            "place": "Любое место в квартире",
            "time": "10:30:00",
            "action": "Есть фрукты",
            "periodicity": "once_day",
            "is_enjoy_habit": "False",
            "time_habit": "120",
            "link_habit": 1,
            "is_public": "True"
        }
        response = self.client.post(
            '/habit/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_destroy_habit(self):
        """Тестирование удаления привычки"""

        Habit.objects.create(
            id=1,
            place="Любое место в квартире",
            time="10:30:00",
            action="Потискать кота",
            periodicity="once_day",
            is_enjoy_habit="True",
            time_habit="60",
            is_public="True",
            owner=self.user
        )

        response = self.client.delete(
            '/habit/delete/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_list_habit(self):
        """Тестирование выведения списка привычек"""

        Habit.objects.create(
            id=1,
            place="Любое место в квартире",
            time="10:30:00",
            action="Потискать кота",
            periodicity="once_day",
            is_enjoy_habit="True",
            time_habit="60",
            is_public="False",
            owner=self.user
        )

        response = self.client.get(
            '/habit/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_list_habit_public(self):
        """Тестирование выведения списка публичных привычек"""

        Habit.objects.create(
            id=1,
            place="Любое место в квартире",
            time="10:30:00",
            action="Потискать кота",
            periodicity="once_day",
            is_enjoy_habit="True",
            time_habit="60",
            is_public="True",
            owner=self.user
        )

        response = self.client.get(
            '/habit/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        """Тестирование обновления информации о привычке"""

        Habit.objects.create(
            id=1,
            place="Любое место в квартире",
            time="10:30:00",
            action="Потискать кота",
            periodicity="once_day",
            is_enjoy_habit="True",
            time_habit="60",
            is_public="True",
            owner=self.user
        )

        data = {
            "time_habit": "100",
            "is_enjoy_habit": "True"
        }

        response = self.client.patch(
            '/habit/update/1/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


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
