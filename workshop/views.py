from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from cart.models import Order
from product.models import Product


# Create your views here.
def home_page(request):
    items = Order.order_manager.get_order_items(request.user)
    context = {
        'items': items
    }
    return render(request, 'workshop/home.html', context)


class ProductManListView(ListView):
    template_name = 'workshop/product_list.html'
    paginate_by = 6

    def get_queryset(self):
        print(self.kwargs)
        products = Product.published.all()
        if Product is not None:
            return products
        else:
            raise Http404("Product not found")


class ProductWomanListView(ListView):
    template_name = 'workshop/product_list.html'
    paginate_by = 6

    def get_queryset(self):
        print(self.kwargs)
        products = Product.published.all()
        if Product is not None:
            return products
        else:
            raise Http404("Product not found")

