from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer, TimeSlotSerializer, BookingSerializer
from ..models import User, Contact, Booking, TimeSlot
from .forms import MyUserCreationForm
from rest_framework import status
from django.contrib.auth import authenticate

@api_view(['GET'])
def main(request):
    msg = ['Nothing Here']
    return Response(msg)

@api_view(['POST'])
def checkEmail(request):
    try:
        User.objects.get(email = request.POST.get('email'))
        sendData = {'error' : 'Email Exists.'}
        return Response(sendData, status=status.HTTP_400_BAD_REQUEST)
    except:
        sendData = {'message' : 'Email Available.'}
        return Response(sendData, status=status.HTTP_200_OK)

@api_view(['POST'])
def registerUser(request):
    form = MyUserCreationForm(request.POST)
    sendData = {}
    if form.is_valid():
        user = form.save()
        user.username = user.username.lower()
        serial = UserSerializer(user, many=False)
        return Response(serial.data, status=status.HTTP_201_CREATED)
    else:
        sendData = {'error' : 'Username Already Exists.'}
    return Response(sendData, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def loginUser(request):
    email = request.POST.get('email').lower()
    password = request.POST.get('password')
    try:
        user = User.objects.get(email = email)
    except:
        sendData = {'error' : 'No User Found in the username.'}
        return Response(sendData, status=status.HTTP_404_NOT_FOUND)
    user = authenticate(request, email=email, password=password)
    if user is not None:
        serial = UserSerializer(user, many=False)
        return Response(serial.data, status=status.HTTP_202_ACCEPTED)
    sendData = {'error' : 'Wrong Password'}
    return Response(sendData, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
def contact(request):
    username = request.POST.get('username')
    message = request.POST.get('message')
    try:
        user = User.objects.get(username = username)
        newMessage = Contact(user = user, message = message)
        newMessage.save()
        return Response({'message' : 'Message Send Successfully.'}, status=status.HTTP_201_CREATED)

    except:
        return Response({'error' : 'Something went wrong.'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def checkSlot(request):
    try:
        date = request.GET.get('date')
        bookings = Booking.objects.filter(date = date)
        slots = TimeSlot.objects.all()
        for i in bookings:
            slots = slots.exclude(id = i.slot.id)
        serializer = TimeSlotSerializer(slots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        sendData = {'error' : 'Something went wrong.'}
        return Response(sendData, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def bookSlot(request):
    try:
        username = request.POST.get('username')
        date = request.POST.get('date')
        time = request.POST.get('slot')
        paymentId = request.POST.get('paymentId')
        user = User.objects.get(username = username)
        slot = TimeSlot.objects.get(time = time)
        amt = slot.amount
        bookedItem = Booking(user = user, date = date, slot = slot, paymentId = paymentId, amt=amt)
        bookedItem.save()
        serialized = BookingSerializer(bookedItem, many=False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    except:
        sendData = {'error' : 'Something went wrong.'}
        return Response(sendData, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def cancelSlot(request):
    try:
        username = request.POST.get('username')
        bookingId = request.POST.get('bookingId')
        booking = Booking.objects.get(id=bookingId)
        if(booking.user.username != username):
            sendData = {'error' : 'Requested User Error'}
            return Response(sendData, status=status.HTTP_401_UNAUTHORIZED)
        booking.delete()
        return Response({'message' : 'Slot Cancelled Successfully.'}, status=status.HTTP_202_ACCEPTED)
    except:
        sendData = {'error' : 'Something Went Wrong.'}
        return Response(sendData, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def editSlot(request):
    try:
        username = request.POST.get('username')
        bookingId = request.POST.get('bookingId')
        time = request.POST.get('slot')
        booking = Booking.objects.get(id=bookingId)
        if(booking.user.username != username):
            sendData = {'error' : 'Requested User Error'}
            return Response(sendData, status=status.HTTP_401_UNAUTHORIZED)
        slot = TimeSlot.objects.get(time = time)
        booking.slot = slot
        booking.save()
        return Response({'message' : 'Slot Edited Successfully.'}, status=status.HTTP_202_ACCEPTED)
    except:
        sendData = {'error' : 'Something Went Wrong.'}
        return Response(sendData, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def viewSlot(request):
    try:
        username = request.POST.get('username')
        user = User.objects.get(username = username)
        bookings = Booking.objects.filter(user = user)
        serialized = BookingSerializer(bookings, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        sendData = {'error' : 'Something went wrong.'}
        return Response(sendData, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def chatBot(request):
    try:
        sendData = {'response' : 'Hello'}
        return Response(sendData, status=status.HTTP_202_ACCEPTED)
    except:
        return Response({'error' : 'Something Went Wrong.'}, status=status.HTTP_400_BAD_REQUEST)