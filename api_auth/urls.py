from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from api_auth.views import CustomTokenObtainPairView


urlpatterns = [
    path('login', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
