from django.shortcuts import render
import pyrebase
from django.core.mail import EmailMessage, send_mail
from theOceanColombo import settings
from django.template.loader import render_to_string
import smtplib

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


def selectroom(request):
    return render(request, 'selectRoom.html')


def loadselectroom(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    roomIDs = db.child('Rooms').shallow().get().val()

    roomIDList = []
    for i in roomIDs:
        roomIDList.append(i)

    roomTypeList = []
    for i in roomIDList:
        type = db.child('Rooms').child(i).child('Room Type').get().val()
        roomTypeList.append(type)

    roomDescList = []
    for i in roomIDList:
        desc = db.child('Rooms').child(i).child('Description').get().val()
        roomDescList.append(desc)

    rooms = zip(roomTypeList, roomDescList)

    return render(request, 'selectroom.html', {'rooms': rooms})


def confirmbooking(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    firstName = request.POST.get('first_name')
    lastName = request.POST.get('last_name')
    email = request.POST.get('email')
    contactNumber = request.POST.get('contactNo')
    NIC = request.POST.get('NIC')

    data = {
        "FirstName": firstName,
        "LastName": lastName,
        "Email": email,
        "ContactNumber": contactNumber,
    }

    db.child("Customer").child("Contact Details").child(NIC).set(data)

    address = request.POST.get('address')
    suburb = request.POST.get('suburb')
    city = request.POST.get('city')
    postalCode = request.POST.get('postalCode')

    data = {
        "Suburb": suburb,
        "City": city,
        "PostalCode": postalCode
    }

    db.child("Payment").child("Billing Address").child(address).set(data)

    fromEmail = settings.EMAIL_HOST_USER
    pwd = settings.EMAIL_HOST_PASSWORD

    emailSubject = 'Your Booking Is Confirmed'
    emailBody = 'Test'
    template = render_to_string(
        'bookingConfirmationEmail.html', {'name': firstName})
    fromEmail = settings.EMAIL_HOST_USER
    confirmMail = EmailMessage(
        emailSubject,
        template,
        fromEmail,
        [email]
    )
    confirmMail.fail_silently = False
    confirmMail.send()

    return render(request, 'bookingSuccessful.html')


def loadconfirmbooking(request):
    checkIn = request.POST.get('checkIn')
    checkOut = request.POST.get('checkOut')
    dates = {
        'checkIn': checkIn,
        'checkOut': checkOut
    }
    return render(request, 'confirmBooking.html', dates)


def cancelbooking(request):
    return render(request, 'cancelBooking.html')


def loadcancelbooking(request):
    return render(request, 'cancelBooking.html')


def updatebooking(request):
    return render(request, 'updateBooking.html')


def loadupdatebooking(request):
    return render(request, 'updateBooking.html')


def loadbookingconfirmed(request):
    return render(request, 'bookingSuccessful.html')
