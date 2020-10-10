from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("newEmployee/", views.Newemployee),
    path("viewEmployee/", views.Viewemployee),
    path("HireNew/", views.loadNewemployee)
]