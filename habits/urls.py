from habits.apps import HabitsConfig
from rest_framework.routers import DefaultRouter
from habits.views import RewardViewSet, HabitCreateAPIView, HabitListAPIView, \
    HabitPublicListAPIView, HabitDestroyAPIView, HabitUpdateAPIView, HabitRetrieveAPIView
from django.urls import path

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'reward', RewardViewSet, basename='reward')

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habit/', HabitListAPIView.as_view(), name='habit-list'),
    path('habit_public/', HabitPublicListAPIView.as_view(), name='habit-public-list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-detail'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
] + router.urls
