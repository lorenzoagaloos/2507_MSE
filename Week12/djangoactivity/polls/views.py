from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
if __name__ == "__main__":
    print(index)  # Example usage of the index view function