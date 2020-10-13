
from django.urls import path
from . import views


urlpatterns = [
    path('selectRoom/', views.loadselectroom),
    path('confirmBooking/', views.loadconfirmbooking),
    path('addBooking/', views.confirmbooking),
    path('cancelBooking/', views.loadcancelbooking),
    path('deleteBooking/', views.cancelbooking),
    path('updateBooking/', views.loadupdatebooking),
    path('editBooking/', views.updatebooking),
    path('bookingConfirmed/', views.loadbookingconfirmed)
]
