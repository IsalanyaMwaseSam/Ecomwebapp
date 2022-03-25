from django.shortcuts import render
from account.models import Account
from homeapp.models import *
import account


def home(request):
    accounts = Account.objects.all()
    products = Product.objects.all()
    context = {'products':products, 'accounts':accounts}
    return render (request, 'homeapp/base.html', context)

def shop(request):
    return render (request, 'homeapp/home.html', {})

def cart(request):
    return render(request, 'homeapp/cart.html', {})