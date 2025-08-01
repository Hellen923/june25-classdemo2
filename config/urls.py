"""
URL configuration for the project.
This module defines the URL patterns for the main project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greeting/', include('greeting.urls')),
]