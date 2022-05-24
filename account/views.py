import email
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm
from django.contrib import messages
from . models import Account
from homeapp.models import Order
from django.views.generic import ListView, View




def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your account was successfully created!'))
            return redirect('home')
        else:
            messages.error(request, ('Invalid input.'))
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        try:
            user = Account.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username Or Password')
    return render(request, 'account/login.html')



