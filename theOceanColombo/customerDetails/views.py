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

def custloign(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    authe = firebase.auth()
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    print(email)
    print(pwd)
    try:
        user = authe.sign_in_with_email_and_password(email, pwd)
    except:
        message = "Invalid username or password please try again"
        return render(request, "customerLogin.html", {"msg": message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "userDetails.html")


# def logout(request):
#     authe = firebase.auth()
#     authe.logout(request)
#     return render(request,'customerLogin.html')

def custreg(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    authe = firebase.auth()
    FName = request.POST.get('fname')
    LName = request.POST.get('lname')
    NIC = request.POST.get('nic')
    Email = request.POST.get('email')
    Phone = request.POST.get('phone')
    Gender = request.POST.get('gender')
    Password = request.POST.get('psw')
    rPassword = request.POST.get('psw-repeat')
    data = {"FirstName": FName, "LastName": LName,  "Email": Email, "ContactNumber": Phone,
            "gender": Gender, "psw": Password, "psw-repeat": rPassword}
    db.child("Customer").child("ContactDetails").child(NIC).set(data)
    authe.create_user_with_email_and_password(Email,Password)

    return render(request, "customerLogin.html")

def loadcustreg(request):
    return render(request, "customerRegistration.html")


def userdetails(request):
    return render(request, "userDetails.html")

def loaduserdetails(request):
    final_data = getcusdata()
    return render(request, "userDetails.html",{'final_data':final_data})

def getcusdata():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child('Customer').child('ContactDetails').shallow().get().val()
    list_cusnic=[]
    for i in data:
        list_cusnic.append(i)

    print(list_cusnic)

    list_cusFname=[]
    list_cusLname=[]
    list_email=[]
    list_phone=[]
   
    for i in list_cusnic:
        query = db.child('Customer').child('ContactDetails').child(i).child('FirstName').get().val()
        list_cusFname.append(query)
    
    print(list_cusFname)

    for i in list_cusnic:
        query = db.child('Customer').child('ContactDetails').child(i).child('LastName').get().val()
        list_cusLname.append(query)

    print(list_cusLname)

    for i in list_cusnic:
        query = db.child('Customer').child('ContactDetails').child(i).child('Email').get().val()
        list_email.append(query)

    print(list_email)

    for i in list_cusnic:
        query = db.child('Customer').child('ContactDetails').child(i).child('ContactNumber').get().val()
        list_phone.append(query)
    
    print(list_phone)

    final_data= zip(list_cusnic,list_cusFname,list_cusLname,list_email,list_phone)
    return final_data  

def updateCustomerDetails(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    FName = request.POST.get('fname')
    LName = request.POST.get('lname')
    NIC = request.POST.get('nic')
    Email = request.POST.get('email')
    Phone = request.POST.get('phone')
    Gender = request.POST.get('gender')

    data = {"fname": FName, "lname": LName, "email": Email, "phone": Phone,
            "gender": Gender}
    db.child("Customer").child("ContactDetails").child(NIC).update(data)


    return render(request, "userDetails.html")

def loadupdateCustomerDetails(request):
    return render(request, 'updateDetailsCus.html')

def deleteCus(request):
        firebase = pyrebase.initialize_app(firebaseconfig)
        db = firebase.database()
        NIC = request.POST.get('NIC')    
        db.child("Customer").child("ContactDetails").child(NIC).remove()

        final_data = getcusdata()
        return render (request,"userDetails.html",{'final_data': final_data})