"""
This module contains the views for the greeting application.
"""
from django.http import HttpResponse

def hello_world(request):
    """
    Handles a request to the hello world page.

    Args:
        request: The HTTP request object.

    Returns:
        An HttpResponse with the text "Hello, World!".
    """
    return HttpResponse("Hello, World!")