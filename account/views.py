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
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, ('Your account was successfully created!'))
            return redirect('/')
        else:
            messages.error(request, ('Invalid input.'))
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})

def userpage(request):
    return render(request, 'homeapp/userpage.html', {})

