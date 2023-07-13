from typing import Any, Dict
from django.shortcuts import render
from .models import Order, Cart
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import OrderForm, CarForm
from products.models import Product
from datetime import datetime
from rest_framework import generics
from .serializer import CartSerializer
from django.http import HttpResponseRedirect


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_create.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        pk = self.kwargs.get("pk")
        form.instance.product = Product.objects.get(pk=pk)
        form.instance.status = "Order Placed"
        form.instance.is_active = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context["product"] = Product.objects.get(pk=pk)
        return context
    

class OrderListView(ListView):
    model = Order
    form_class = OrderForm
    template_name = 'order_list.html'
    context_object_name = 'yourmodels'


class OrderDetailView(DetailView):
    model = Order
    form_class = OrderForm
    template_name = 'order_detail.html'
    context_object_name = 'yourmodel'


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_update.html'
    success_url = reverse_lazy('product_list')


class OrderDeleteView(DeleteView):
    model = Order
    form_class = OrderForm
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('yourmodel_list')


#Cart Views

class AddtoCartView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        product = self.kwargs["product"]
        quantity = self.kwargs["quantity"]
        product_details = Product.objects.get(pk=product)
        price = product_details.price * quantity
        serializer.save(user=self.request.user, product = product, quantity= quantity, price = price)
        return HttpResponseRedirect('/cart')
    

class ListCartView(ListView):
    model = Order
    form_class = CarForm
    template_name = 'order/cart_list.html'
    context_object_name = 'yourmodels'


class DeletfromCartView(DeleteView):
    model = Order
    form_class = CarForm
    template_name = 'order/cart_confirm_delete.html'
    success_url = reverse_lazy('yourmodel_list')


class UpdateCartView(UpdateView):
    model = Order
    form_class = CarForm
    template_name = 'order/cart_update.html'
    success_url = reverse_lazy('product_list')