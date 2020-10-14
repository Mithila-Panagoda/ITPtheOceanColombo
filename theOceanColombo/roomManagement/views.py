from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

import pyrebase
import uuid

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


def dirRoomManagementHome(request):
    return render(request, "RoomManagementHome.html")


def InsertRoomDetails(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    roomNo = request.POST.get('roomNumber')
    roomType = request.POST.get('roomType')
    description = request.POST.get('description')
    roomImage = request.POST.get('image')
    price = request.POST.get('price')

    # push data
    data = {"RoomNo": roomNo, "RoomType": roomType, "Price": price, "Description": description,
            "RoomImage": roomImage}
    db.child("Rooms").child(roomNo).set(data)
    return render(request, "InsertRoomDetails.html")


def dirBackendHome(request):
    return render(request, "BackendHome.html")


def InsertRooms(request):
    return render(request, "roomDetails.html")


def getRoomDetails():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("Rooms").shallow().get().val()

    list_roomNumber = []
    list_roomNo = []
    list_roomType = []
    list_description = []
    list_price = []

    for j in data:
        list_roomNumber.append(j)

    for j in list_roomNumber:
        roomNo = db.child("Rooms").child(j).child("RoomNo").get().val()
        list_roomNo.append(roomNo)

    for j in list_roomNumber:
        type = db.child("Rooms").child(j).child("RoomType").get().val()
        list_roomType.append(type)

    for j in list_roomNumber:
        description = db.child("Rooms").child(j).child("Description").get().val()
        list_description.append(description)

    for j in list_roomNumber:
        price = "Rs. " + db.child("Rooms").child(j).child("Price").get().val()
        list_price.append(price)

    data = zip(list_roomNo, list_roomType, list_description, list_price)
    return data


def roomDetails(request):
    data = getRoomDetails()
    return render(request, "roomDetails.html", {'data': data})


def UpdateRoomDetails(request):
    roomNo = request.POST.get('roomNo')
    data = getSingleRoomData(roomNo)
    return render(request, "UpdateRoomDetails.html", {'data': data})


def getSingleRoomData(RoomNo):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    list_roomNo = []
    list_roomType = []
    list_description = []
    list_price = []
    list_roomNo.append(RoomNo)
    list_roomNo.append(db.child("Rooms").child(RoomNo).child("RoomNo").get().val())
    list_roomType.append(db.child("Rooms").child(RoomNo).child("RoomType").get().val())
    list_description.append(db.child("Rooms").child(RoomNo).child("Description").get().val())
    list_price.append(db.child("Rooms").child(RoomNo).child("Price").get().val())
    data = zip(list_roomNo, list_roomType, list_description, list_price)
    return data


def dirUpdateRoomDetails(request):
    return render(request, "UpdateRoomDetails.html")


def UpdateRoomDetailsToDB(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    roomNo = request.POST.get('roomNumber')
    roomType = request.POST.get("roomType")
    description = request.POST.get("description")
    price = request.POST.get("price")
    data1 = {"RoomNo": roomNo, "RoomType": roomType, "Description": description, "Price": price}
    db.child("Rooms").child(roomNo).update(data1)
    data = getRoomDetails()
    return render(request, "roomDetails.html", {'data': data})


def deleteRoom(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("Housekeeping").shallow().get().val()
    list_roomNumber = []

    for j in data:
        list_roomNumber.append(j)

    roomNo = request.POST.get('roomNo')

    for j in list_roomNumber:
        if roomNo != db.child("Housekeeping").child(j).child("RoomNo").get().val():
            db.child("Rooms").child(roomNo).remove()
    data = getRoomDetails()
    return render(request, "roomDetails.html", {'data': data})

def dirInsertAssignedEmployees(request):
    return render(request, "statusAndAssignmentOfEmployees.html")


def InsertAssignedEmployees(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data1 = db.child("Rooms").shallow().get().val()

    list_roomNumber = []

    for j in data1:
        list_roomNumber.append(j)

    assigningDate = request.POST.get('assigningDate')
    roomNumber1 = request.POST.get('roomNumber')
    status = request.POST.get('status')
    condition = request.POST.get('condition')
    assigningTime = request.POST.get('assigningTime')
    assignedEmployee = request.POST.get('employee')
    date = uuid.uuid1()

    # push data
    for j in list_roomNumber:
        if roomNumber1 == db.child("Rooms").child(j).child("RoomNo").get().val():
            data = {"AssignedDate": assigningDate, "RoomNo": roomNumber1, "Status": status, "Condition": condition,
                    "AssignedTime": assigningTime, "AssignedEmployee": assignedEmployee}
            db.child("Housekeeping").child(date).set(data)
    return render(request, "statusAndAssignmentOfEmployees.html")


def getHousekeepingDetails():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("Housekeeping").shallow().get().val()
    data1 = db.child("Rooms").shallow().get().val()

    list_id = []
    list_roomNumber = []
    list_roomNo = []
    list_assignedEmployee = []
    list_assignedTime = []
    list_condition = []
    list_status = []
    list_roomType = []

    for j in data:
        list_id.append(j)

    for j in data1:
        list_roomNumber.append(j)

    for i in list_id:
        for j in list_roomNumber:
            if db.child("Housekeeping").child(i).child("RoomNo").get().val() == db.child("Rooms").child(j).child("RoomNo").get().val():
                roomType = db.child("Rooms").child(j).child("RoomType").get().val()
                list_roomType.append(roomType)

    for j in list_id:
        if db.child("Housekeeping").child(j).child("Condition").get().val() == "Dirty":
            if db.child("Housekeeping").child(j).child("AssignedDate").get().val() == str(
                    datetime.date(datetime.now())):
                roomNo = db.child("Housekeeping").child(j).child("RoomNo").get().val()
                list_roomNo.append(roomNo)

    for j in list_id:
        if db.child("Housekeeping").child(j).child("Condition").get().val() == "Dirty":
            if db.child("Housekeeping").child(j).child("AssignedDate").get().val() == str(
                    datetime.date(datetime.now())):
                assignedEmployee = db.child("Housekeeping").child(j).child("AssignedEmployee").get().val()
                list_assignedEmployee.append(assignedEmployee)

    for j in list_id:
        if db.child("Housekeeping").child(j).child("Condition").get().val() == "Dirty":
            if db.child("Housekeeping").child(j).child("AssignedDate").get().val() == str(
                    datetime.date(datetime.now())):
                assignedTime = db.child("Housekeeping").child(j).child("AssignedTime").get().val()
                list_assignedTime.append(assignedTime)
    list_assignedTime.sort(reverse=False)

    for j in list_id:
        if db.child("Housekeeping").child(j).child("Condition").get().val() == "Dirty":
            if db.child("Housekeeping").child(j).child("AssignedDate").get().val() == str(
                    datetime.date(datetime.now())):
                Condition = db.child("Housekeeping").child(j).child("Condition").get().val()
                list_condition.append(Condition)

    for j in list_id:
        if db.child("Housekeeping").child(j).child("Condition").get().val() == "Dirty":
            if db.child("Housekeeping").child(j).child("AssignedDate").get().val() == str(
                    datetime.date(datetime.now())):
                status = db.child("Housekeeping").child(j).child("Status").get().val()
                list_status.append(status)

    data = zip(list_roomNo, list_roomType, list_status, list_assignedEmployee, list_assignedTime)
    return data


def housekeepingDetails(request):
    data = getHousekeepingDetails()
    return render(request, "HousekeepingReport.html", {'data': data})

def getDetailsByRoomType(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    data = db.child("Rooms").shallow().get().val()

    list_roomNumber = []
    list_roomType = []
    list_roomNo = []
    list_description = []
    list_price = []

    for j in data:
        list_roomNumber.append(j)

    for j in list_roomNumber:
        if request.POST.get('roomType1') == db.child("Rooms").child(j).child("RoomType").get().val():
                roomNo = db.child("Rooms").child(j).child("RoomNo").get().val()
                list_roomNo.append(roomNo)

    for j in list_roomNumber:
        if request.POST.get('roomType1') == db.child("Rooms").child(j).child("RoomType").get().val():
            type = db.child("Rooms").child(j).child("RoomType").get().val()
            list_roomType.append(type)

    for j in list_roomNumber:
        if request.POST.get('roomType1') == db.child("Rooms").child(j).child("RoomType").get().val():
            description = db.child("Rooms").child(j).child("Description").get().val()
            list_description.append(description)

    for j in list_roomNumber:
        if request.POST.get('roomType1') == db.child("Rooms").child(j).child("RoomType").get().val():
            price = "Rs. " + db.child("Rooms").child(j).child("Price").get().val()
            list_price.append(price)

    data = zip(list_roomNo, list_roomType, list_description, list_price)
    return render(request, "roomDetails.html", {'data': data})

