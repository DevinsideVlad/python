from django import forms

from products.models import Product, Basket


class QuantityForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'block_quantity__number', 'placeholder': '1', 'min': 1,
    }))

    class Meta:
        model = Basket
        fields = ('quantity',)

