from django.shortcuts import render
from .models import Product


def all_products(request):
    '''A view to return all products and handle searching
    and filtering etc.'''
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "home/index.html", context)
