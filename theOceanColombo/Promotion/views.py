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
    final_data = GetEmp()
    return render(request, "PromoManagement.html",{'final_data':final_data})
#Update Employee
def Updatepromo (request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    EPF = request.POST.get('EPF')
    First_Name= request.POST.get('firstName')
    Title = request.POST.get('Title')
    Employment_type = request.POST.get('employeeType')
    data = {"firstName": First_Name, "Title": Title, "employeeType":Employment_type}
    db.child("Staff").child("Employee").child(EPF).update(data)
    final_data = GetEmp()
    return render(request, "PromoManagement.html",{'final_data':final_data})

def loadUpdatepromo (request):
    return render(request, "UpdatePromo.html")
#Retrieve and View Employee
def GetEmp():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child('Staff').child('Employee').shallow().get().val()
    list_empepf=[]
    for i in data:
        list_empepf.append(i)

    print(list_empepf)


    list_empFname=[]
    list_title=[]
    list_Emptype=[]

    for i in list_empepf:
        query = db.child('Staff').child('Employee').child(i).child('firstName').get().val()
        list_empFname.append(query)

    for i in list_empepf:
        query = db.child('Staff').child('Employee').child(i).child('Title').get().val()
        list_title.append(query) 

    for i in list_empepf:
        query = db.child('Staff').child('Employee').child(i).child('employeeType').get().val()
        list_Emptype.append(query)

    final_data= zip(list_empepf,list_empFname,list_title,list_Emptype)
    return final_data