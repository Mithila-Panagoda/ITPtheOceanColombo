from django.urls import path
from . import views

urlpatterns = [
    path("HousekeepingReport/", views.dirHousekeepingReport),
    path("continuousReport/", views.dirContinuousReport),
    path("InsertRoomDetails/", views.InsertRoomDetails),
    path("roomDetails/", views.dirRoomDetails),
    path("roomManagementHome/", views.dirRoomManagementHome),
    path("updateRoomDetails/", views.dirUpdateRoomDetails),
    path('InsertRooms', views.InsertRooms, name="InsertRooms"),
    path("backendHome/", views.dirBackendHome),
]
