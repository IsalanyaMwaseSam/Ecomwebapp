from django.urls import path
from .views import (
    HomeView,
    CartView,
    shop,
    add_to_cart

)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('homeapp/', shop, name='homeapp'),
    path('homeapp/cart/<slug>', CartView.as_view(), name='cart'),
    path('homeapp/add-to-cart/<slug>', add_to_cart, name='add-to-cart')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)