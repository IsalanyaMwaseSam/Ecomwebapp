import email
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm
from django.contrib import messages
from .models import Account



def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = request.POST['first_name']
            other_names =  request.POST['other_names']
            email =  request.POST['email']
            username = request.POST['username']
            raw_password =  request.POST['password1']
            phonenumber =  request.POST['phonenumber']
            Address_1 =  request.POST['Address_1']
            Address_2 =  request.POST['Address_2']
            user = Account.objects.create_user(first_name=first_name, other_names=other_names, email=email, username=username, password=raw_password, phonenumber=phonenumber, Address_1=Address_1, Address_2=Address_2)
            user.save()
            messages.success(request, ('Your account was successfully created!'))
            login(request, user)
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

