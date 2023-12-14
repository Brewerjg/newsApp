from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),  # URL pattern for the homepage and tech page
]