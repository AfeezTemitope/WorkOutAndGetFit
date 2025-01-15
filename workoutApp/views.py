import os

import requests
from django.http import JsonResponse
from dotenv import load_dotenv
from rest_framework.viewsets import ModelViewSet

from workoutApp.models import CustomUser
from workoutApp.serializers import CreateUserSerializer

load_dotenv()
# Create your views here.


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer


def fitness_data(request):
    url = 'https://api.api-ninjas.com/v1/nutrition?query=1lb brisket and fries'
    headers = {
        "X-api-key": os.getenv('FITNESS_DATA')
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return JsonResponse(response.json(), safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def total_calories_burn_in_a_week(self, calories_burn):
        workout_type = 'skiing'
        api_url = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'.format(workout_type)
        headers = {
            'X-api-key': os.getenv('API_KEY')
        }
        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == requests.codes.ok:
                print(response.text)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)



