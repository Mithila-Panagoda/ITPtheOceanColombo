from django.shortcuts import render
from django.shortcuts import render
from django.http import request, HttpResponse
import pyrebase
from xhtml2pdf import pisa

# Create your views here.
from django.template.loader import get_template

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
    final_data = getDriverDetails()
    return render(request, "InsertVehicle.html", {"final_data": final_data})


def insertvehicle(request):  # code not implemented
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    NUMBER_PLATE = request.POST.get('NUMBER_PLATE')
    VEHICLE_MODEL = request.POST.get('VEHICLEMODEL')
    NOOFSEATS = request.POST.get('noOfSeats')
    dname = request.POST.get('dname')
    data = {"Vehicle_Model": VEHICLE_MODEL, "No_Of_Seats": NOOFSEATS, "Driver name": dname, "Number plate": NUMBER_PLATE}

    db.child('Vehicle').child(NUMBER_PLATE).set(data)
    final_list = showvehicledetails()
    return render(request, 'AvailableVehicleList.html', {'final_list': final_list})


# Retrieve inserted Vehicle details

def loadavailablev(request):
    final_list = showvehicledetails()
    return render(request, "AvailableVehicleList.html", {'final_list': final_list})


def showvehicledetails():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    number_plate = db.child('Vehicle').shallow().get().val()
    list_vids = []
    for i in number_plate:
        list_vids.append(i)
    print(list_vids)

    list_vmode = []
    for i in list_vids:
        vehicle_mode = db.child('Vehicle').child(i).child('Vehicle_Model').get().val()
        list_vmode.append(vehicle_mode)
    print(list_vmode)

    list_no_seats = []
    for i in list_vids:
        no_of_seats = db.child('Vehicle').child(i).child('No_Of_Seats').get().val()
        list_no_seats.append(no_of_seats)
    print(list_no_seats)

    list_DriverName = []
    for i in list_vids:
        query = db.child('Vehicle').child(i).child('Driver name').get().val()
        list_DriverName.append(query)

    comb_list = zip(list_vids, list_vmode, list_no_seats, list_DriverName)
    return comb_list


# Update Vehicle

def getsingleVehicle(number_plate):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    list_vids = []
    list_vids.append(number_plate)

    list_vmode = [db.child("Vehicle").child(number_plate).child("Vehicle_Model").get().val()]

    list_no_seats = []
    list_no_seats.append(db.child("Vehicle").child(number_plate).child("No_Of_Seats").get().val())

    list_driver = []
    query = db.child('Vehicle').child(number_plate).child('Driver name').get().val()
    list_driver.append(query)

    comb_list = zip(list_vids, list_vmode, list_no_seats, list_driver)
    return comb_list


def updatevehicle(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    NUMBER_PLATE = request.POST.get('NUMBER_PLATE')
    VEHICLE_MODEL = request.POST.get('VEHICLEMODEL')
    NOOFSEATS = request.POST.get('noOfSeats')
    dname = request.POST.get('dname')

    data = {"Vehicle_Model": VEHICLE_MODEL, "No_Of_Seats": NOOFSEATS, "Driver name": dname}

    db.child('Vehicle').child(NUMBER_PLATE).update(data)

    final_list = showvehicledetails()
    return render(request, "AvailableVehicleList.html", {'final_list': final_list})


def loadaupdatev(request):
    number_plate = request.POST.get('number_plate')
    final_list = getsingleVehicle(number_plate)
    return render(request, "UpdateVehicle.html", {"final_list": final_list})


# Deleting details of a vehicle
def deletevehicle(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    number_plate = request.POST.get('number_plate')
    print(number_plate)
    db.child('Vehicle').child(number_plate).remove()
    final_list = showvehicledetails()
    return render(request, "AvailableVehicleList.html", {"final_list": final_list})


##########
def getDriverDetails():
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    data = db.child("Staff").child("Employee").shallow().get().val()
    list_EmpID = []
    for i in data:
        list_EmpID.append(i)

    list_DriverName = []
    for i in list_EmpID:
        if db.child("Staff").child("Employee").child(i).child("Title").get().val() == "Driver":
            Query = db.child("Staff").child("Employee").child(i).child("firstName").get().val()
            list_DriverName.append(Query)
    return list_DriverName


def dirBackendHome(request):
    return render(request, "BackendHome.html")


def generateVehicleReport(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()

    data = db.child("Staff").child("Employee").shallow().get().val()
    list_EmpID = []
    for i in data:
        list_EmpID.append(i)

    list_DriverName = []
    for i in list_EmpID:
        if db.child("Staff").child("Employee").child(i).child("Title").get().val() == "Driver":
            Query = db.child("Staff").child("Employee").child(i).child("firstName").get().val()
            list_DriverName.append(Query)

    number_plate = db.child('Vehicle').shallow().get().val()
    list_vids = []
    for i in number_plate:
        list_vids.append(i)

    list_vehicleModel = []
    for i in list_DriverName:
        for j in list_vids:
            if db.child("Vehicle").child(j).child("Driver name").get().val() == i:
                model = db.child("Vehicle").child(j).child("Vehicle_Model").get().val()
                list_vehicleModel.append(model)

    list_numPlates = []
    for i in list_DriverName:
        for j in list_vids:
            if db.child("Vehicle").child(j).child("Driver name").get().val() == i:
                numPlates = db.child("Vehicle").child(j).child("Number plate").get().val()
                list_numPlates.append(numPlates)

    data = zip(list_DriverName, list_vehicleModel, list_numPlates)

    template_path = 'VehicleReport.html'
    context = {'data': data, 'numper_plate': number_plate}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Discription'] = 'attachment;filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    if pisa_status.err:
        return HttpResponse('Oops!We had some errors<prev>' + html + '</prev>')
    return response
