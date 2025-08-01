"""
This module defines the models for the greeting app.
"""
from django.db import models

class Greeting(models.Model):
    """
    A model to store greetings.
    """
    message = models.CharField(max_length=200)

    def __str__(self):
        """String representation of the Greeting object."""
        return self.message