from rest_framework.serializers import ModelSerializer
from base.models import User, TimeSlot, Booking

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','name', 'email', 'phone']

class TimeSlotSerializer(ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'