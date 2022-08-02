from homeapp.models import Product
from django import forms

class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'seller', 'discount_price', 'description', 'characteristics', 'specifications', 'image1', 'image2', 'image3', 'image4', 'slug']