from itertools import product
from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib import messages
from homeapp.models import Product
from sales.forms import AddProduct

# Create your views here.
def sell(request):
    form = AddProduct(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your Product has successfully been added!")  
    context = {
    'form': form,
    'username': 'seller: ' + str(request.user),
    }  
    return render(request, 'sales/sell.html', context)

def activate(request):
    return render(request, 'sales/activate_account.html', {})

