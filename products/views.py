from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Product, Category
from .forms import ProductForm, CategoryForm


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create.html'
    success_url = '/product_list/'


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_create.html'
    success_url = '/category_list/'


class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'products/category_update.html'
    fields = ['name', 'description']  # Specify the fields to include in the form
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'products/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
