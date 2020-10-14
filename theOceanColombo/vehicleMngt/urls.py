from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("loadvehicle/", views.loadinsertvehicle),
    path("addVehicle/", views.insertvehicle),
    path("loadshowvehicle/" , views.loadavailablev),
    path("showavailblev/", views.showvehicledetails),
    path("loadupdatev/", views.loadaupdatev),
    path("updateVh/", views.updatevehicle),
    path("deletev/", views.deletevehicle),
    path("repov/",views.getDriverDetails),
    path("backendHome/", views.dirBackendHome),
    path("report/", views.generateVehicleReport)
    #path("availableL", view.)
]