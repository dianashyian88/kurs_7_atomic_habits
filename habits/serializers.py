from rest_framework import serializers
from habits.models import Reward, Habit
from habits.validators import TimeHabitValidator, LinkHabitHabitValidator


class RewardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reward
        fields = '__all__'
        validators = [TimeHabitValidator(field='time_habit')]


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [TimeHabitValidator(field='time_habit'),
                      LinkHabitHabitValidator(field='link_habit'),
                      ]

    def validate(self, attrs):
        is_enjoy_habit, link_habit, reward = \
            attrs.get('is_enjoy_habit', True), \
            attrs.get('link_habit', None), \
            attrs.get('reward', None)
        if is_enjoy_habit is False and link_habit is None and reward is None:
            raise serializers.ValidationError('Необходимо выбрать '
                                              'связанную привычку '
                                              'или указать вознаграждение')
        elif is_enjoy_habit is False \
                and link_habit is not None \
                and reward is not None:
            raise serializers.ValidationError('У привычки не может быть '
                                              'одновременно связанной '
                                              'привычки '
                                              'и вознаграждения')
        elif is_enjoy_habit is True \
                and link_habit is not None \
                and reward is not None:
            raise serializers.ValidationError('Приятная привычка не может '
                                              'иметь связанную привычку '
                                              'и/или вознаграждение')
        elif is_enjoy_habit is True \
                and link_habit is None \
                and reward is not None:
            raise serializers.ValidationError('Приятная привычка не может '
                                              'иметь связанную привычку '
                                              'и/или вознаграждение')
        elif is_enjoy_habit is True \
                and link_habit is not None \
                and reward is None:
            raise serializers.ValidationError('Приятная привычка не может '
                                              'иметь связанную привычку '
                                              'и/или вознаграждение')
        return attrs
