from django.forms import ModelForm
from ..models import User, Contact
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'phone', 'name', 'password2']