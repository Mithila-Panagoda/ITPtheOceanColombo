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


def loadadddrink(request):
    return render(request, "addbeverage.html")


def adddrink(request):  # code not implemented
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    name = request.POST.get('name')
    price = request.POST.get('price')
    size = request.POST.get('size')
    desc = request.POST.get('desc')
    type = request.POST.get('drink')
    data = {"price": price, "size": size, "desc": desc, "type": type}
    db.child("resturant").child("beverages").child(name).set(data)
