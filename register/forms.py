from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login

class NewUserForm(UserCreationForm):
    first_name=forms.CharField(max_length=60, required=True)
    last_name=forms.CharField(max_length=60, required=True)
    username=forms.CharField(max_length=15, required=True)
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
    def clean(self):
        cleaned_data= super(NewUserForm, self). clean()
        if len(cleaned_data['first_name']) < 2:
            self.add_error("first_name", "First name must be at least 2 characters")
        if len (cleaned_data['last_name']) < 2:            
            self.add_error("last_name", "Last name must be at least 2 characters")


class LogForm(forms.Form):
    username= forms.CharField(max_length=60, required=True)
    password=forms.CharField(min_length=8, widget=forms.PasswordInput)