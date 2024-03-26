from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .models import Product, ProductGallery


# Create your views here.
def product_pk(request, uid):
    product = Product.published.get_by_uid(uid)
    product_uid = str(uid).replace('{', '').replace('}', '')
    product_slug = str(product.slug)
    url = reverse_lazy('product:product_detail', args=[product_uid, product_slug])
    return redirect(url)


def product_detail(request, uid, slug):
    product = Product.published.get_product(uid, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product/product_detail.html', context)
