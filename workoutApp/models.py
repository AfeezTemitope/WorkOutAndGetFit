import random
from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from paystacks.customers import Customer


class CustomUser(AbstractUser):
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    otp = models.EmailField(unique=True, blank=True)

    def __str__(self):
        return self.username


# Define the available workout types
class WorkoutType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    WORKOUT_TYPES = [
        ('squats', 'Squats'),
        ('step_ups', 'Step Ups'),
        ('lunges', 'Lunges'),
        ('push_ups', 'Push Ups'),
        ('wall_sits', 'Wall Sits'),
        ('dips', 'Dips'),
    ]
    workout_types = models.CharField(max_length=20, choices=WORKOUT_TYPES)

    def __str__(self):
        return self.name


# Define different exercise types
class ExerciseType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    EXERCISE_TYPES = [
        ('squats', 'Squats'),
        ('step_ups', 'Step Ups'),
        ('lunges', 'Lunges'),
        ('push_ups', 'Push Ups'),
    ]
    exercise_types = models.CharField(max_length=10, choices=EXERCISE_TYPES)

    def __str__(self):
        return self.name


# Represents an individual exercise performed by the user
class Exercise(models.Model):
    user = models.ForeignKey('workoutApp.CustomUser', on_delete=models.CASCADE, related_name='exercises')
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return f'{self.user.name} - {self.exercise_type.name}'


# Represents a workout session performed by the user
class Workout(models.Model):
    user = models.ForeignKey('workoutApp.CustomUser', on_delete=models.CASCADE,
                             related_name='workouts')  # Added ForeignKey to User
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE, related_name='workouts')
    duration = models.DurationField()
    calories_burn = models.IntegerField()
    workout_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user} - {self.workout_type.name} ({self.workout_date})'


# Represents the user's fitness goals
class Goals(models.Model):
    user = models.ForeignKey('workoutApp.CustomUser', on_delete=models.CASCADE, related_name='goals')
    description = models.CharField(max_length=255)
    target_date = models.DateField()

    def __str__(self):
        return f"{self.user.name}'s goal: {self.description}"


# Represents user's access levels in the application
class AbstractUser(Customer):
    MEMBERSHIP_CHOICES = [
        ('P', 'Premium'),
        ('G', 'Gold'),
        ('B', 'Basic')
    ]
    membership = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES)


class Consultants(models.Model):
    full_name = models.CharField(max_length=100)
    otp = models.EmailField(unique=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)
    license_number = models.CharField(max_length=15)
    field_specialisation = models.CharField(max_length=10, blank=True)
    health_institution = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.full_name


class LiveSession(models.Model):

    user = models.ForeignKey('workoutApp.CustomUser', on_delete=models.CASCADE, related_name='live_sessions')
    consultants = models.ForeignKey(Consultants, on_delete=models.CASCADE, related_name='livesessions')
    user = models.ForeignKey('workoutApp.CustomUser', on_delete=models.CASCADE, related_name='sessions')
    consultants = models.ForeignKey('workoutApp.Consultants', on_delete=models.CASCADE, related_name='livesessions')  # Make sure 'Consultants' is correctly referenced

    def __str__(self):
        return f"Session with {self.consultants.full_name} for {self.user.username}"


class UserDistance(models.Model):
    user = models.ForeignKey('workoutApp.CustomUser', on_delete=models.CASCADE, related_name='distance')
    date = models.DateField(default=date.today)
    total_distance = models.FloatField(default=0.0)
    last_location = models.JSONField(default=dict)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f'{self.user.username} - {self.date} - {self.total_distance} km'


