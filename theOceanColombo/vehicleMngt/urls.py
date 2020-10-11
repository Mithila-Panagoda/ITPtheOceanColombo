from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("loadvehicle/", views.loadinsertvehicle),
    path("addVehicle/", views.insertvehicle),
    path("loadshowvehicle/" , views.loadavailablev),
    path("showavailblev/", views.loadavailablev),
     #path("loadupdate/", views.loadupdatevehicle),
    #path("updateVehicle/", views.updateVehicle)
]