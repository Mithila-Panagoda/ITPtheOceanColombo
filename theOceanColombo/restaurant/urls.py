from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("loaddrink/",views.loadadddrink),
    path("addDrink/",views.adddrink)
]