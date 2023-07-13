from django.forms import ModelForm
from .models import Order, Cart


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ("quantity",)


class CarForm(ModelForm):
    class Meta:
        model = Cart
        fields = ("quantity",)
