from operator import truediv

from django.test import TestCase

from django.test import Client

from workoutApp import models
from workoutApp.views import CustomUserViewSet

# Create your tests here.

crsf_client = Client(enforce_csrf_checks=True)
def test_that_fitness_data_received(client):
    assert models.CustomUser.objects.exists == True

def test_that_fitness_data_sent(client):
    assert models.CustomUser.objects.count() == 1

def test_that_user_can_register(customUser):
    customUser.set_password('<PASSWORD>')
    customUser.set_email('walex5347@gmail.com')
    customUser.set_first_name('John')
    customUser.set_last_name('Doe')
    customUser.set_height(6.23)
    customUser.set_weight(10)
    customUser.set_age(20)
    customUser.set_gender('female')
    response = customUser.save()
    assert models.CustomUser.objects.count() == 1
    assert response == "User has been successfully registered"