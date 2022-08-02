from django import forms
from account.models import Account
from homeapp.models import Product


class SearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name']

class BillingForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'other_names', 'phonenumber', 'Address', 'Town']