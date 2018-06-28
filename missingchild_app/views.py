# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import Sign_Up_Form
from .forms import Upload_Form
from .models import Child
from .models import Profile

@login_required
def home(request):
    child = Child.objects.all()
    print Child.objects.values('image')
    return render(request, 'home.html',{'child':child})

def signup(request):
    if request.method =='POST':
        form = Sign_Up_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = Sign_Up_Form()
    return render(request, 'signup.html', {'form': form})


def upload(request):
    if request.method =='POST':
        upload_form = Upload_Form(request.POST,request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            return redirect('home')
    else:
        upload_form = Upload_Form()
    return render(request, 'upload.html',{'upload_form':upload_form})

def report(request):
    # profile = Profile.objects.filter(user__username =request.user)
    child = Child.objects.filter(user__user__username = request.user)
    print dir(Child)
    return render(request,"report.html", {'child':child})
