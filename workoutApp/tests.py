from operator import truediv

from django.test import TestCase

from django.test import Client

from workoutApp import models

# Create your tests here.

crsf_client = Client(enforce_csrf_checks=True)
def test_that_fitness_data_received(client):
    assert models.CustomUser.objects.exists == true
