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
    Emergency_Contact = request.POST.get('EmergencyCon')
    data = {"firstName": First_Name, "lastName": Last_Name, "NIC": NIC, "Title": Title, "employeeType": Employment_type,
            "Email": Email, "Address": Address, "Phone": Phone, "EmergencyCon": Emergency_Contact}
    db.child("Staff").child("Employee").child(EPF).set(data)
    authe.create_user_with_email_and_password(Email, Password)
    return render(request, "ViewEmployee.html")


def loadNewemployee(request):
    return render(request, "NewEmployee.html")


def Viewemployee(request):
    return render(request, "ViewEmployee.html")


def loadViewemployee(request):
    final_data = getempdata()
    return render(request, "ViewEmployee.html", {'final_data': final_data})


def getempdata():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child('Staff').child('Employee').shallow().get().val()
    list_empepf = []
    for i in data:
        list_empepf.append(i)

    print(list_empepf)

    list_empFname = []
    list_empLname = []
    list_nic = []
    list_title = []
    list_Emptype = []
    list_email = []
    list_adrs = []
    list_phone = []
    list_EmergCont = []

    for i in list_empepf:
        query = db.child('Staff').child('Employee').child(
            i).child('firstName').get().val()
        list_empFname.append(query)

    print(list_empFname)

    for i in list_empepf:
        query = db.child('Staff').child('Employee').child(
            i).child('lastName').get().val()
        list_empLname.append(query)

    for i in list_empepf:
        query = db.child('Staff').child(
            'Employee').child(i).child('NIC').get().val()
        list_nic.append(query)

    for i in list_empepf:
        query = db.child('Staff').child('Employee').child(
            i).child('Title').get().val()
        list_title.append(query)

    for i in list_empepf:
        query = db.child('Staff').child('Employee').child(
            i).child('employeeType').get().val()
        list_Emptype.append(query)

    for i in list_empepf:
        query = db.child('Staff').child('Employee').child(
            i).child('Email').get().val()
        list_email.append(query)

    for i in list_empepf:
        query = db.child("Staff").child('Employee').child(
            i).child("Address").get().val()
        list_adrs.append(query)

    for i in list_empepf:
        query = db.child("Staff").child('Employee').child(
            i).child("Phone").get().val()
        list_phone.append(query)

    for i in list_empepf:
        query = db.child("Staff").child('Employee').child(
            i).child("EmergencyCo").get().val()
        list_EmergCont.append(query)

    final_data = zip(list_empepf, list_empFname, list_empLname, list_nic, list_title,
                     list_Emptype, list_email, list_adrs, list_phone, list_EmergCont)
    return final_data


def deleteEmp(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    empepf = request.POST.get('empEPF')
    db.child("Staff").child("Employee").child(empepf).remove()
    final_data = getempdata()
    return render(request, "ViewEmployee.html", {'final_data': final_data})
