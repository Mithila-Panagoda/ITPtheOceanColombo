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

def Newemployee(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    authe = firebase.auth()
    db = firebase.database()
    First_Name = request.POST.get('firstName')
    Last_Name = request.POST.get('lastName')
    NIC = request.POST.get('NIC')
    Title = request.POST.get('Title')
    Employment_type = request.POST.get('employeeType')
    Email = request.POST.get('Email')
    Password = request.POST.get('Password')
    Address = request.POST.get('Address')
    Phone = request.POST.get('Phone')
    EPF = request.POST.get('EPF')
    Emergency_Contact= request.POST.get('EmergencyCon')
    data = {"firstName": First_Name, "lastName": Last_Name, "NIC": NIC, "Title": Title,"employeeType": Employment_type,
            "Email": Email, "Address": Address, "Phone":Phone,"EmergencyCon":Emergency_Contact}
    db.child("Staff").child("Employee").child(EPF).set(data)
    authe.create_user_with_email_and_password(Email,Password)
    return render(request, "ViewEmployee.html")

def loadNewemployee(request):
    return render(request, "NewEmployee.html")

def Viewemployee(request):
    return render(request, "ViewEmployee.html")

def loadViewemployee(request):
    return render(request, "ViewEmployee.html")