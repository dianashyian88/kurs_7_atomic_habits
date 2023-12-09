from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users.apps import UsersConfig
from users.views import RegistrationAPIView, LoginAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
    path('registration/', RegistrationAPIView.as_view(),
         name='user-registration'),
    path('login/', LoginAPIView.as_view(),
         name='user-login'),
]
