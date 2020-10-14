from django.shortcuts import render
import pyrebase
from django.core.mail import EmailMessage, send_mail
from theOceanColombo import settings
from django.template.loader import render_to_string
import smtplib
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime

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

    print(roomIDList)

    roomTypeList = []
    for i in roomIDList:
        type = db.child('Rooms').child(i).child('RoomType').get().val()
        roomTypeList.append(type)

    roomDescList = []
    for i in roomIDList:
        desc = db.child('Rooms').child(i).child('Description').get().val()
        roomDescList.append(desc)

    roomPriceList = []
    for i in roomIDList:
        price = db.child('Rooms').child(i).child('Price').get().val()
        roomPriceList.append(price)

    rooms = zip(roomTypeList, roomDescList, roomPriceList)

    return render(request, 'selectroom.html', {'rooms': rooms})


def confirmbooking(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    firstName = request.POST.get('first_name')
    lastName = request.POST.get('last_name')
    email = request.POST.get('email')
    contactNumber = request.POST.get('contactNo')
    NIC = request.POST.get('NIC')
    checkIn = request.POST.get('checkIn')
    checkOut = request.POST.get('checkOut')
    ETA = request.POST.get('ETA')
    roomName = request.POST.get('roomName')
    roomQty = request.POST.get('roomQty')
    roomCost = request.POST.get('roomCost')
    roomTotal = request.POST.get('roomTotal')
    splRequests = request.POST.get('splRequests')

    contactDetails = {
        "FirstName": firstName,
        "LastName": lastName,
        "Email": email,
        "ContactNumber": contactNumber,
    }

    db.child("Customer").child("Contact Details").child(
        NIC).set(contactDetails)

    rooms = {
        "RoomQty": roomQty,
        "TotalCost": roomTotal
    }

    db.child("Customer").child("Contact Details").child(
        NIC).child("Rooms").child(roomName).set(rooms)

    booking = {
        "CheckIn": checkIn,
        "CheckOut": checkOut,
        "ETA": ETA,
        "SpecialRequests": splRequests
    }

    db.child("Customer").child("Contact Details").child(
        NIC).child("BookingDetails").set(booking)

    arrivals = {
        "ETA": ETA,
        "Special Requests": splRequests,
        "RoomName": roomName,
        "RoomQty": roomQty,
        "Total": roomTotal,
    }

    db.child("Arrivals").child(checkIn).child(NIC).set(arrivals)

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

    data = {
        "NIC": NIC,
        'name': firstName,
        'checkIn': checkIn,
        'checkOut': checkOut,
        'roomType': roomName,
        'roomTotal': roomTotal,
        'roomQty': roomQty
    }

    emailSubject = 'Your Booking Is Confirmed'
    emailBody = 'Test'
    template = render_to_string(
        'bookingConfirmationEmail.html', data)
    fromEmail = settings.EMAIL_HOST_USER
    confirmMail = EmailMessage(
        emailSubject,
        template,
        fromEmail,
        [email]
    )
    confirmMail.fail_silently = False
    confirmMail.send()

    return render(request, 'bookingSuccessful.html', {"NIC": NIC})


def loadconfirmbooking(request):
    checkIn = request.POST.get('checkIn')
    checkOut = request.POST.get('checkOut')
    roomName = request.POST.get('roomName')
    roomQty = request.POST.get('roomQty')
    roomCost = request.POST.get('roomCost')
    roomTotal = request.POST.get('roomTotal')
    bookingInfo = {
        'checkIn': checkIn,
        'checkOut': checkOut,
        'roomName': roomName,
        'roomQty': roomQty,
        'roomCost': roomCost,
        'roomTotal': roomTotal
    }
    return render(request, 'confirmBooking.html', bookingInfo)


def cancelbooking(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    NIC = request.POST.get('NIC')
    print(NIC)
    reason = request.POST.get('cancelReason')
    try:
        db.child('Customer').child('Contact Details').child(NIC).remove()
    except:
        print('unable to delete')

    db.child('RoomBookingCancellationReason').child(
        NIC).set({'Reason': reason})

    return render(request, 'bookingCancelSuccessful.html', {"NIC": NIC})


def loadcancelbooking(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    NIC = request.POST.get('NIC')

    checkIn = db.child('Customer').child('Contact Details').child(
        NIC).child('BookingDetails').child('CheckIn').get().val()
    checkOut = db.child('Customer').child('Contact Details').child(
        NIC).child('BookingDetails').child('CheckOut').get().val()

    roomNames = db.child('Customer').child('Contact Details').child(
        NIC).child('Rooms').shallow().get().val()

    roomsList = []
    for i in roomNames:
        roomsList.append(i)

    qtyList = []
    for i in roomsList:
        qty = db.child('Customer').child('Contact Details').child(
            NIC).child('Rooms').child(i).child('RoomQty').get().val()
        qtyList.append(qty)

    totalList = []
    for i in roomsList:
        total = db.child('Customer').child('Contact Details').child(
            NIC).child('Rooms').child(i).child('TotalCost').get().val()
        totalList.append(total)

    rooms = zip(roomsList, qtyList, totalList)
    data = {
        "NIC": NIC,
        "checkIn": checkIn,
        "checkOut": checkOut,
        "rooms": rooms
    }

    return render(request, 'cancelBooking.html', data)


def updatebooking(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    NIC = request.POST.get('NIC')
    checkIn = request.POST.get('checkIn')
    checkOut = request.POST.get('checkOut')

    data = {
        "CheckIn": checkIn,
        "CheckOut": checkOut
    }
    db.child('Customer').child('Contact Details').child(NIC).child(
        'BookingDetails').update(data)

    return render(request, 'bookingUpdateSuccessful.html')


def loadupdatebooking(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    NIC = request.POST.get('NIC')

    checkIn = db.child('Customer').child('Contact Details').child(
        NIC).child('BookingDetails').child('CheckIn').get().val()
    checkOut = db.child('Customer').child('Contact Details').child(
        NIC).child('BookingDetails').child('CheckOut').get().val()

    roomNames = db.child('Customer').child('Contact Details').child(
        NIC).child('Rooms').shallow().get().val()

    roomsList = []
    for i in roomNames:
        roomsList.append(i)

    qtyList = []
    for i in roomsList:
        qty = db.child('Customer').child('Contact Details').child(
            NIC).child('Rooms').child(i).child('RoomQty').get().val()
        qtyList.append(qty)

    totalList = []
    for i in roomsList:
        total = db.child('Customer').child('Contact Details').child(
            NIC).child('Rooms').child(i).child('TotalCost').get().val()
        totalList.append(total)

    rooms = zip(roomsList, qtyList, totalList)
    data = {
        "NIC": NIC,
        "checkIn": checkIn,
        "checkOut": checkOut,
        "rooms": rooms
    }

    return render(request, 'updateBooking.html', data)


def loadbookingconfirmed(request):
    return render(request, 'bookingSuccessful.html')


def generateArrivalReport(request):
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    NICs = db.child('Arrivals').child(tomorrow).shallow().get().val()

    NICList = []

    for i in NICs:
        NICList.append(i)

    ETAList = []
    for i in NICList:
        ETA = db.child('Arrivals').child(
            tomorrow).child(i).child('ETA').get().val()
        ETAList.append(ETA)

    requestList = []
    for i in NICList:
        request = db.child('Arrivals').child(
            tomorrow).child(i).child('Special Requests').get().val()
        requestList.append(request)

    roomList = []
    for i in NICList:
        room = db.child('Arrivals').child(
            tomorrow).child(i).child('RoomName').get().val()
        roomList.append(room)

    qtyList = []
    for i in NICList:
        qty = db.child('Arrivals').child(
            tomorrow).child(i).child('RoomQty').get().val()
        qtyList.append(qty)

    totalList = []
    for i in NICList:
        total = db.child('Arrivals').child(
            tomorrow).child(i).child('Total').get().val()
        totalList.append(total)

    info = zip(NICList, ETAList, requestList, roomList, qtyList, totalList)

    template_path = 'arrivalReport.html'
    context = {'date': tomorrow, 'info': info}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
