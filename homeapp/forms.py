from django import forms
from homeapp.models import Product


class SearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name']