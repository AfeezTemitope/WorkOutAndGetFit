from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workoutApp.views import CustomUserViewSet, fitness_data, total_calories_burn_in_a_week
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('register', CustomUserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('fitness/', fitness_data, name='fitness_data'),

    path('workout/', total_calories_burn_in_a_week, name='calories_burn_in_a_week')
]
