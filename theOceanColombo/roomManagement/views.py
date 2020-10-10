from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

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
authe = firebase.auth()
storage = firebase.storage()

def dirContinuousReport(request):
    return render(request, "continuousReport.html")


def dirHousekeepingReport(request):
    return render(request, "HousekeepingReport.html")


def dirInsertRoomDetails(request):
    return render(request, "InsertRoomDetails.html")


def dirRoomDetails(request):
    return render(request, "roomDetails.html")

def roomDetails(request):
    db = firebase.database()
    #rooms = db.child("Rooms").get()
    #print(rooms.val())
    return render(request, 'roomDetails.html', {'content': db.child("Rooms").get()})

def dirRoomManagementHome(request):
    return render(request, "RoomManagementHome.html")

def InsertRoomDetails(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    roomNo = request.POST.get('roomNumber')
    roomType = request.POST.get('roomType')
    accommodationType = request.POST.getlist('accommodationType')
    description = request.POST.get('description')
    roomImage = request.POST.get('image')

    #push data
    data = {"Room Number" : roomNo, "Room Type" : roomType, "AccommodationType" : accommodationType, "Description" : description, "Room Image" : roomImage}
    db.child("Rooms").child(roomNo).set(data)
    return render(request, "InsertRoomDetails.html")

def dirBackendHome(request):
    return render(request, "BackendHome.html")


def InsertRooms(request):
    return render(request, "roomDetails.html")

def dirUpdateRoomDetails(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    roomNo = request.POST.get('roomNumber')
    roomType = request.POST.get('roomType')
    description = request.POST.get('description')
    roomImage = request.POST.get('image')

    # push data
    data = {"Room Number": roomNo, "Room Type": roomType, "Description": description, "Room Image": roomImage}
    db.child("Rooms").child(roomNo).update(data)
    return render(request, "UpdateRoomDetails.html")


