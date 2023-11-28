from django.shortcuts import render
from .models import User, Booking, Contact


def loginPage(request):
    content = {}
    return render(request, 'base/login_register.html', content)

def orderPage(request):
    orders = Booking.objects.all()
    content = {'page' : 'Orders', 'tabulated' : True, 'orders' : orders}
    return render(request, 'base/orders.html', content)

def userPage(request):
    users = User.objects.all()
    content = {'page' : 'Users', 'tabulated' : True, 'users' : users}
    return render(request, 'base/users.html', content)

def statisticPage(request):
    content = {'page' : 'Statistics'}
    return render(request, 'base/statistics.html', content)

def profilePage(request):
    username = request.GET.get('username') if request.GET.get('username') != None else 'admin'
    user = User.objects.get(username = username)
    bookings = Booking.objects.filter(user = user)[:5]
    content = {'page' : 'Profile', 'user' : user, 'orders':bookings}
    return render(request, 'base/profile.html', content)

def inboxPage(request):
    contacts = Contact.objects.all()
    content = {'page' : 'Inbox', 'messages' : contacts}
    return render(request, 'base/inbox.html', content)

def slotPage(request):
    content = {'page' : 'Slots'}
    return render(request, 'base/slots.html', content)