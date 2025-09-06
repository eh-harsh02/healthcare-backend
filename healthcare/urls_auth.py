from django.urls import path
from .views_auth import register, login

urlpatterns = [
    path('auth/register/', register, name='register'),
    path('auth/login/', login, name='login'),
]
