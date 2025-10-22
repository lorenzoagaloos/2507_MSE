"""A Django view that returns a personalized welcome message."""
from django.http import HttpResponse

def welcome(request, name):

    name = "Lily"
    
    return HttpResponse(f"<h1>Welcome {name} to Django!</h1>")

