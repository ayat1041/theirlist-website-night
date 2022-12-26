from django.urls import path
from .views import *
# app_name = "app"

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('facebook/',HomeView.as_view(),name='facebook'),
]