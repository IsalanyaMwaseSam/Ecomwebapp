from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views as user_views
from . import views



urlpatterns = [
    path('account/login/', auth_views.LoginView.as_view(template_name = 'account/login.html'), name='login'),
    path('account/register/',views.registration, name='registration'),
    path('account/logout/', auth_views.LogoutView.as_view(template_name = 'account/logout.html'), name='logout'),
    path('userpage/', views.userpage, name='userpage'),
    
  

]