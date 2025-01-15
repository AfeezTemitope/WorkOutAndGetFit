from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workoutApp.views import CustomUserViewSet, fitness_data, OTPVerification
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register('register', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/verify-otp/', OTPVerification.as_view(), name='verify-otp'),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='login route'),
    path('auth/token/blacklist/', jwt_views.TokenBlacklistView.as_view(), name='logout route'),

    path('fitness/', fitness_data, name='fitness_data'),

]
