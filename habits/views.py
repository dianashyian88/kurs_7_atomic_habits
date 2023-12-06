from rest_framework import viewsets, generics
from habits.models import Reward, Habit
from habits.serializers import RewardSerializer, HabitSerializer
from habits.permissions import IsOwner, ViewPublicHabits
from habits.pagination import HabitsPaginator
from rest_framework.permissions import IsAuthenticated


class RewardViewSet(viewsets.ModelViewSet):
    """ViewSet для вознаграждений"""
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()
    permission_classes = [IsOwner]
    pagination_class = HabitsPaginator

    def perform_create(self, serializer):
        """Функция сохраняет id пользователя, который создает вознаграждение, в поле owner"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def list(self, request, *args, **kwargs):
        """Функция позволяет отфильтровать вознаграждения по пользователю и выводить данные постранично"""
        queryset = Reward.objects.filter(owner=request.user)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = RewardSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class HabitCreateAPIView(generics.CreateAPIView):
    """Эндпойнт создания привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Функция сохраняет id пользователя, который создает привычку, в поле owner"""
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпойнт выведения информации об одной привычке"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner | ViewPublicHabits]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Эндпойнт обновления привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Эндпойнт удаления привычки"""
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitListAPIView(generics.ListAPIView):
    """Эндпойнт выведения списка привычек с пагинацией"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
    pagination_class = HabitsPaginator

    def list(self, request, *args, **kwargs):
        """Функция позволяет отфильтровать привычки по пользователю и выводить данные постранично"""
        queryset = Habit.objects.filter(owner=request.user)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class HabitPublicListAPIView(generics.ListAPIView):
    """Эндпойнт выведения списка публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
