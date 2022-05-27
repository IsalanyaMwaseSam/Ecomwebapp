from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from account.models import Account
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from homeapp.forms import SearchForm
from homeapp.models import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required



class HomeView(ListView):
    model = Product
    template_name = 'homeapp/home.html'

class CartView(DetailView):
    model = Product
    template_name = 'homeapp/product.html'

class shopView(LoginRequiredMixin, View):
    login_url='/account/login/'
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'homeapp/cart.html', context)
        except ObjectDoesNotExist:
            return redirect("/")

@login_required(login_url='/account/login/')
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
            messages.info(request, "This item quantity was updated.")
            return redirect("homeapp:cart")
        else:
            order.products.add(order_product)
            messages.info(request, "This item was added to your cart.")
            return redirect("homeapp:product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
    return redirect("homeapp:product",slug=slug)
   
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
            messages.info(request, "This item was not in your cart")
            return redirect("homeapp:product",slug=slug) 
            
    else:
        messages.info(request, "This item was not in your cart")
        return redirect("homeapp:cart",slug=slug)    
    return redirect("homeapp:product",slug=slug)

@login_required
def remove_single_product_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()
            else:
                order.products.remove(order_product)
            messages.info(request, "This item quantity was updated.")
            return redirect("homeapp:cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("homeapp:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("homeapp:product", slug=slug)


