"""
This module contains the configuration for the greeting app.
"""
from django.apps import AppConfig

class GreetingConfig(AppConfig):
    """
    Configuration class for the greeting app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'greeting'