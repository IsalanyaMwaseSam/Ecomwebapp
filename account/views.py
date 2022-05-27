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
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        try:
            user = Account.objects.get(email=email)
        except:
            messages.error(request, 'email does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email Or Password')
    return render(request, 'account/login.html')



