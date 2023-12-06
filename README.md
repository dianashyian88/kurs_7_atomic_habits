Контекст
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.

В рамках учебного курсового проекта выполнена реализация бэкенд-части SPA веб-приложения.

Критерии приемки курсовой работы:
+Решение выложили на GitHub.
+Имеется список зависимостей.
+Настроили CORS.
+Использовали переменные окружения.
+Все необходимые модели описаны или переопределены.
+Реализовали пагинацию.
+Описанные права доступа заложены.
+Настроили все необходимые валидаторы (чтоб валидация работала, поле при создании нужно явно заполнять):
+Исключить одновременный выбор связанной привычки и указания вознаграждения.
+Время выполнения должно быть не больше 120 секунд.
+В связанные привычки могут попадать только привычки с признаком приятной привычки.
+У приятной привычки не может быть вознаграждения или связанной привычки.
+Нельзя выполнять привычку реже, чем 1 раз в 7 дней (реализовано на уровне модели в наборе вариантов)
+-Все необходимые эндпоинты реализовали. (еще необходима регистрация и авторизация пользователей)

Настроили интеграцию с Telegram.
Настроили отложенную задачу через Celery.

Проект покрыли тестами как минимум на 80%.

Код оформили в соответствии с лучшими практиками.
Результат проверки Flake8 равен 100%, при исключении миграций.
