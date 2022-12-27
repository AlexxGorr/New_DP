from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductsList(ListView):
    # model = Product
    # ordering = 'name'

    queryset = Product.objects.filter(price__lt = 300)
    tamplate_name = 'products.html'
    context_object_name = 'products'









