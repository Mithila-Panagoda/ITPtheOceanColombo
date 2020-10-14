from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("newEmployee/", views.Newemployee),
    path("viewEmployee/", views.loadViewemployee),
    path("HireNew/", views.loadNewemployee),
    path("deletemp/",views.deleteEmp)
]