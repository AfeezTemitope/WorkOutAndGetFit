from decimal import Decimal

from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from workoutApp.models import Workout, Goals, Exercise, CustomUser, WorkoutType


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'age', 'gender', 'weight', 'height', 'email', 'password']


class WorkoutTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutType
        fields = ['name', 'workout_types']


class WorkoutSerializer(serializers.ModelSerializer):
    workout_type = WorkoutTypeSerializer()
    calories_burn = serializers.SerializerMethodField(method_name='calculate_calories_burn')

    class Meta:
        model = CustomUser
        fields = ['age', 'weight', 'height']

    def calculate_calories_burn(self, customUser: CustomUser):
        return Decimal(7.38) * customUser.weight + (607 * customUser.height) - (Decimal(2.31) * customUser.age) + 43


class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = ['user', 'description', 'target_date']


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'





