from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Booking)
admin.site.register(models.Contact)
admin.site.register(models.TimeSlot)
admin.site.register(models.Offer)