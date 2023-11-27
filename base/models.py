from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username
    
class TimeSlot(models.Model):
    time = models.TimeField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return str(self.time)
    
class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True)
    paymentId = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message
    
class Offer(models.Model):
    date = models.DateField()
    slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return self.amount