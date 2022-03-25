from django.urls import path
from .views import (
    HomeView,
    CartView,
    shop

)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('homeapp/', shop, name='homeapp'),
    path('homeapp/cart/<slug>', CartView.as_view(), name='cart')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)