import random
from decimal import Decimal

from django.core.mail import send_mail
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from workoutApp.models import Workout, Goals, Exercise, CustomUser, WorkoutType


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


#STEPS TO DEPLOYMENT ON RENDER
# INSTALL pip install uvicorn gunicorn on your project terminal
# install pip install dj-database-url , This package allows us to transform the database URL into Django database parameters.
# Add this to requirements.txt file, like this; dj-database-url==2.3.0
# Your 'DATABASE_URL': dj_database_url.parse(os.getenv('DATABASE_URL'), conn_max_age=600), will be in this format under DATABASES SETTINGS
# To collect static files and migrate the database, we'll create a build script
# Type your  pip install -r requirements.txt command again...
# Add STATIC_ROOT = os.path.join(BASE_DIR, 'static') to your settings.py under STATIC_URL
# Run python manage.py collectstatic --no-input
# Run python manage.py migrate to migrate all changes...
#


