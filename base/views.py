from django.shortcuts import redirect, render
from .models import User, Booking, Contact, TimeSlot
from datetime import date, timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from .forms import SlotForm


def loginPage(request):
    content = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        try:
            user = User.objects.get(email = username)
        except Exception as e:
            print(e)
            return render(request, 'base/login_register.html', {'message' : 'User Doesn\'t Exists'})
        
        if not user.is_superuser:
            return render(request, 'base/login_register.html', {'message' : 'Not Allowed Here'})
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('order-page')
        return render(request, 'base/login_register.html', {'message' : 'Wrong Password'})
    return render(request, 'base/login_register.html', content)

@login_required(login_url='login-page')
def orderPage(request):
    orders = Booking.objects.all()
    content = {'page' : 'Orders', 'tabulated' : True, 'orders' : orders}
    return render(request, 'base/orders.html', content)

@login_required(login_url='login-page')
def userPage(request):
    users = User.objects.all()
    content = {'page' : 'Users', 'tabulated' : True, 'users' : users}
    return render(request, 'base/users.html', content)

@login_required(login_url='login-page')
def statisticPage(request):
    td = date.today()
    bookings = Booking.objects
    sendData = {}
    for i in range(7):
        sendData[td-timedelta(days=i)] = (bookings.filter(date = td-timedelta(days=i)).count()/13)*100
    content = {'page' : 'Statistics', 'statistics' : sendData}
    return render(request, 'base/statistics.html', content)

@login_required(login_url='login-page')
def profilePage(request):
    username = request.GET.get('username') if request.GET.get('username') != None else 'admin'
    user = User.objects.get(username = username)
    bookings = Booking.objects.filter(user = user)[:5]
    content = {'page' : 'Profile', 'user' : user, 'orders':bookings}
    return render(request, 'base/profile.html', content)

@login_required(login_url='login-page')
def inboxPage(request):
    contacts = Contact.objects.all()
    content = {'page' : 'Inbox', 'messages' : contacts}
    return render(request, 'base/inbox.html', content)

@login_required(login_url='login-page')
def slotPage(request):
    slots = TimeSlot.objects.all()
    content = {'page' : 'Slots', 'slots' : slots}
    if request.method == 'POST':
        time = request.POST.get('time')
        amt = request.POST.get('amt')
        slot = TimeSlot.objects.get(time = time)
        slot.amount = amt
        slot.save()
        content['message'] = True
        return render(request, 'base/slots.html', content)
    return render(request, 'base/slots.html', content)

def userLogout(request):
    logout(request)
    return redirect('/')