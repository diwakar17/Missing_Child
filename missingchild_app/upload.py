from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class Sign_Up_Form(UserCreationForm):
#     name = forms.CharField(max_length=30, required=True,help_text='Optional.')
#     second_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
#     email = forms.EmailField(max_length=50,required=True, help_text='Required. Inform a valid email address.')
#     date_of_birth = forms.DateField(help_text= 'Required .')
#     phone_number = forms.CharField(max_length=13)
