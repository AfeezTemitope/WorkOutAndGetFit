import random
from decimal import Decimal

from django.core.mail import send_mail
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from workoutApp.models import Workout, Goals, Exercise, CustomUser, WorkoutType, Consultants, UserDistance


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'age', 'gender', 'weight', 'height', 'email', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        otp = random.randint(100000, 999999)
        user.otp = otp
        user.save()

        send_mail(
            'Your ONE TIME PASSWORD',
            f'Your OTP CODE is {otp}. NB: this code expires in 15minutes',
            'workoutFitapp@gmail.com',
            [user.email],
            fail_silently=False,
        )
        return user


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


class ConsultantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultants
        fields = ['full_name', 'phone_number', 'field_specialization', 'health_institution']


class UserDistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDistance
        fields = ['user', 'date', 'total_distance', 'last_location']
