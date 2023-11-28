from django.forms import ModelForm
from .models import TimeSlot

class SlotForm(ModelForm):
    class Meta:
        model = TimeSlot
        fields = '__all__'
