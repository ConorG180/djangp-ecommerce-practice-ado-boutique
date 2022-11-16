from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    '''A view to return all products and handle searching
    and filtering etc.'''

    products = Product.objects.all()
    queries = None

    if request.GET:
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter anything.....")
                return redirect(reverse("products"))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": queries,
        "current_categories": categories,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    '''A view to return product details'''

    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)
