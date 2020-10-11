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


# Insert Vehicle
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
    final_list = showvehicledetails()
    return render(request, 'AvailableVehicleList.html',{'final_list':final_list})

#Retrieve inserted Vehicle details

def loadavailablev(request):
    final_list = showvehicledetails()
    return  render(request, "AvailableVehicleList.html", {'final_list' : final_list})

def showvehicledetails():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db=firebase.database()

    number_plate=db.child('Vehicle').shallow().get().val()
    list_vids=[]
    for i in number_plate:
        list_vids.append(i)
    print(list_vids)

    list_vmode=[]
    for i in list_vids:
        vehicle_mode=db.child('Vehicle').child(i).child('Vehicle_Model').get().val()
        list_vmode.append(vehicle_mode)
    print(list_vmode)

    list_no_seats=[]
    for i in list_vids:
        no_of_seats=db.child('Vehicle').child(i).child('No_Of_Seats').get().val()
        list_no_seats.append(no_of_seats)
    print(list_no_seats)

    comb_list = zip(list_vids, list_vmode, list_no_seats)
    return  comb_list

# Update Vehicle

def loadupdatevehicle(request):
    return render(request, "UpdateVehicle.html")


def updateVehicle(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    NUMBER_PLATE = request.POST.get('NUMBER_PLATE')
    VEHICLE_MODEL = request.POST.get('VEHICLEMODEL')
    NOOFSEATS = request.POST.get('noOfSeats')
    data = {"Vehicle_Model": VEHICLE_MODEL, "No_Of_Seats": NOOFSEATS}
    db.child('Vehicle').child(NUMBER_PLATE).update(data)
    getdate = db.child("Vehicle").child(NUMBER_PLATE).child(NUMBER_PLATE).get()
    for task in getdate.each():
        print(task.val())
        print(task.key())
    return render(request, "AvailableVehicleList.html")

# Create your views here.
