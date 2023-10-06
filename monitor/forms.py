from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['product_name', 'desired_price', 'url', 'selector_element']
