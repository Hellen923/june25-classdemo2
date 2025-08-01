from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    """
    Handles a request to the hello world page.
    Returns a simple HTTP response with the text "Hello, World!".
    """
    return HttpResponse("Hello, World!")