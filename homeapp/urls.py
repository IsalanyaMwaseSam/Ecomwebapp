from django.urls import path
from .views import (
    HomeView,
    CartView,
    add_to_cart,
    remove_from_cart,
    remove_single_product_from_cart,

)
from . import views
from django.conf import settings
from django.conf.urls.static import static
from homeapp.views import shopView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('homeapp/product/<slug>', CartView.as_view(), name='product'),
    path('homeapp/add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('homeapp/remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('homeapp/cart', shopView.as_view(), name='cart'),
    path('remove-product-from-cart/<slug>/', remove_single_product_from_cart, name='remove-single-product-from-cart'),
   

   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)