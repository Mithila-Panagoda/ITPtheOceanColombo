from django.urls import path
from . import views

urlpatterns = [
    path("HousekeepingReport/", views.dirHousekeepingReport),
    path("continuousReport/", views.dirContinuousReport),
    path("InsertRoomDetails/", views.InsertRoomDetails),
    path("roomDetails/", views.roomDetails),
    path("roomManagementHome/", views.dirRoomManagementHome),
    path("updateRoomDetails/", views.UpdateRoomDetails),
    path('InsertRooms', views.InsertRooms, name="InsertRooms"),
    path("backendHome/", views.dirBackendHome),
    path("updateDataInDB/", views.UpdateRoomDetailsToDB),
    path("deleteRoom/", views.deleteRoom)
]
