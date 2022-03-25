from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from account.models import Account
from crispy_forms.helper import FormHelper


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'first name'}))
    other_names = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'other names'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    phonenumber = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial="UG"))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email'}), help_text='Required. Add a valid email address')
    Address_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    Address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Region, City'}))

    class Meta:
        model = Account
        fields = ('first_name', 'other_names', 'email', 'username', 'password1', 'password2', 'phonenumber', 'Address_1', 'Address_2')




