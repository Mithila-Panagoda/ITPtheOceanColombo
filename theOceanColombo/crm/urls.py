from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path("loadmessages/", views.loadmessages),
    path("loadsendmessages/", views.loadaddsendmessages)

]