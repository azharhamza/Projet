from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Creeruser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','email','password2']