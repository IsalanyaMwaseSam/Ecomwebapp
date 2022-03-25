from django.shortcuts import render
from account.models import Account
from django.views.generic import ListView, DetailView
from homeapp.models import *

import account


class HomeView(ListView):
    model = Product
    template_name = 'homeapp/home.html'

class CartView(DetailView):
    model = Product
    template_name = 'homeapp/product.html'

def shop(request):
    return render (request, 'homeapp/home.html', {})

