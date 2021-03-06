from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from .models import Product
from django.db.models import Q


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)    
    
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual products """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)