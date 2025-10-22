from django.urls import path

from . import w12a4_django

urlpatterns = [
    path("", templates.index, name="index"),
]