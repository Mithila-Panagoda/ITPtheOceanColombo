from django.urls import path
from . import views


urlpatterns = [
    path('selectRoom/', views.loadselectroom),
    path('confirmBooking/', views.loadconfirmbooking),
    path('addBooking/', views.confirmbooking),
    path('cancelBooking/', views.loadcancelbooking),
    path('updateBooking/', views.loadupdatebooking),
    path('bookingConfirmed/', views.loadbookingconfirmed)
]
