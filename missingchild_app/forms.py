from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Child

class Sign_Up_Form(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,help_text='Optional.')
    second_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=50,required=True, help_text='Required. Inform a valid email address.')
    
    # date_of_birth = forms.DateField(help_text= 'Required .')
    # phone_number = forms.CharField(max_length=13)


class Meta:
        model = User
        fields ={'username', 'first_name', 'second_name', 'email',}

class Upload_Form(forms.ModelForm):
    class Meta:
            model = Child
            fields ={'name','age','details','image'}
