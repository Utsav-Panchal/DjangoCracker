from django.contrib import admin
from django.urls import path
from .views import Hello_World

urlpatterns = [
    path('', Hello_World),
]
