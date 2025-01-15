import os

import requests
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from dotenv import load_dotenv
from workoutApp.models import CustomUser
from workoutApp.serializers import CreateUserSerializer

load_dotenv()
# Create your views here.


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer


class OTPVerification(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if not otp or not email:
            return Response({'detail': 'otp and email are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user.otp == int(otp):
            user.is_active = True
            user.save()
            return Response({'detail': 'Account activated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)


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


