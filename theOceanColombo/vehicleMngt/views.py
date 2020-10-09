from django.shortcuts import render
from django.shortcuts import render
from django.http import request
import pyrebase

# Create your views here.
firebaseconfig = {
    'apiKey': "AIzaSyBew42hA7iZHy7zs47WMqIg-GSBnxP-ttM",
    'authDomain': "theoceancolombo-c128a.firebaseapp.com",
    'databaseURL': "https://theoceancolombo-c128a.firebaseio.com",
    'projectId': "theoceancolombo-c128a",
    'storageBucket': "theoceancolombo-c128a.appspot.com",
    'messagingSenderId': "925636680144",
    'appId': "1:925636680144:web:da1ab5d4f3b0d3231b01d5",
    'measurementId': "G-YH7TV23J8J"
}
firebase = pyrebase.initialize_app(firebaseconfig)


def loadinsertvehicle(request):
    return render(request, "InsertVehicle.html")


def insertvehicle(request):  # code not implemented
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    NUMBER_PLATE = request.POST.get('NUMBER_PLATE')
    VEHICLE_MODEL = request.POST.get('VEHICLEMODEL')
    NOOFSEATS = request.POST.get('noOfSeats')
    data = {"Vehicle_Model": VEHICLE_MODEL, "No_Of_Seats": NOOFSEATS}

    db.child('Vehicle').child(NUMBER_PLATE).set(data)
    return render(request, 'AvailableVehicleList.html')

# Create your views here.

