from django.shortcuts import render
from .models import User


def loginPage(request):
    content = {}
    return render(request, 'base/login_register.html', content)

def orderPage(request):
    content = {'page' : 'Orders', 'tabulated' : True}
    return render(request, 'base/orders.html', content)

def userPage(request):
    content = {'page' : 'Users', 'tabulated' : True}
    return render(request, 'base/users.html', content)

def statisticPage(request):
    content = {'page' : 'Statistics'}
    return render(request, 'base/statistics.html', content)

def profilePage(request):
    content = {'page' : 'Profile'}
    return render(request, 'base/profile.html', content)

def inboxPage(request):
    content = {'page' : 'Inbox'}
    return render(request, 'base/inbox.html', content)

def slotPage(request):
    content = {'page' : 'Slots'}
    return render(request, 'base/slots.html', content)