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

def Promomanagement(request):
    return render(request, "PromoManagement.html")

def loadPromomanagement(request):
    return render(request, "PromoManagement.html")

def Updatepromo (request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    EPF = request.POST.get('EPF')
    First_Name= request.POST.get('firstName')
    Title = request.POST.get('Title')
    data = {"firstName": First_Name, "Title": Title}
    db.child("Staff").child("Employee").child(EPF).update(data)
    return render(request, "PromoManagement.html")

def loadUpdatepromo (request):
    return render(request, "UpdatePromo.html")