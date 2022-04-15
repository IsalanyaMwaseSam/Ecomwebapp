from django.shortcuts import redirect, render, get_object_or_404
from account.models import Account
from django.views.generic import ListView, DetailView
from django.utils import timezone
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

def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_product, created = OrderProduct.objects.get_or_create(product=product,
        user=request.user,
        ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__slug=product.slug).exists():
            order_product.quantity += 1
            order_product.save()
        else:
            order.products.add(order_product)
            
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
    return redirect("homeapp:cart",slug=slug)
   
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProduct.objects.filter(product=product,
                user=request.user,
                ordered=False)[0]
            order.products.remove(order_product)
        else:
            return redirect("homeapp:cart",slug=slug) 
            
    else:
        return redirect("homeapp:cart",slug=slug)    
    return redirect("homeapp:cart",slug=slug)



