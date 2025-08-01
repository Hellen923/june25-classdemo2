"""
This module registers models for the Django Admin site.
"""
from django.contrib import admin
from .models import Greeting

admin.site.register(Greeting)