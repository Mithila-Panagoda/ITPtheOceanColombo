from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("newEmployee/", views.Newemployee),
    path("viewEmployee/", views.loadViewemployee),
    path("HireNew/", views.loadNewemployee),
     path("deletemp/",views.deleteEmp)
]