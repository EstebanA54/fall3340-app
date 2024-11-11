from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "Email", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'something@domain.com'}))
    firstName = forms.CharField(label = "First Name", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    lastName = forms.CharField(label = "Last Name", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))