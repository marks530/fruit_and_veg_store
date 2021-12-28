from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request, product_id):
    """ A view to show all products, including sorting and search queries """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)

def product_detail(request):
    """ A view to show all products, including sorting and search queries """

    product = Product.objects.all()
    context = {
        'product': product,
    }
    return render(request, 'product/product_detail.html', context)