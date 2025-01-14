import os

import requests
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from dotenv import load_dotenv
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


