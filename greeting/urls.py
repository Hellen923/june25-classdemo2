"""
URL configuration for the greeting app.
This module defines the URL patterns for handling requests related to greetings.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_world, name="hello"),
]