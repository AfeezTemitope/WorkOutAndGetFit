from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workoutApp.views import CustomUserViewSet, TrackDistance, fitness_data, OTPVerification, total_calories_burn_in_a_week, exercise_types_and_instructions, get_user_transactions, initialize_user_transaction
from rest_framework_simplejwt import views as jwt_views
from workoutApp.strava import *


router = DefaultRouter()
router.register('register', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/verify-otp/', OTPVerification.as_view(), name='verify-otp'),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='login route'),
    path('auth/token/blacklist/', jwt_views.TokenBlacklistView.as_view(), name='logout route'),

    path('fitness/', fitness_data, name='fitness_data'),
    path('track-distance/', TrackDistance.as_view(), name='track-distance'),
    path('strava/authenticate/', strava_authenticate, name='strava_authenticate'),
    path('strava/callback/', strava_callback, name='strava_callback'),
    path('strava/activities/', fetch_strava_activities, name='strava_activities'),

    path('exercise/', exercise_types_and_instructions, name='exercise_and_instructions'),
    path('workout/', total_calories_burn_in_a_week, name='calories_burn'),

    path('user_transactions/', get_user_transactions, name='transactions'),

    path('paystacks/initiate_transactions', initialize_user_transaction, name='initiate_transactions'),
]
