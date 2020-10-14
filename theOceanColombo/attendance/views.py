from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import request
import pyrebase
from django.contrib import auth
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



def attendance(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    authe = firebase.auth()

    return render(request, "attendance.html")

def loadattendance(request):
    return render(request, "attendance.html")

def viewattendance(request):
    return render(request, "viewAttendance.html")

def loadviewattendance(request):
    return render(request, "viewAttendance.html")