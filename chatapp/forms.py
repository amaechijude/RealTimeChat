from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

#

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        exclude = ['output']

class RoomForm(forms.Form):
    room_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder":"create or join room"}))
