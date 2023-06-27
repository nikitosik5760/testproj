from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from .models import Product


class ShopList(ListView):
    model = Product
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
