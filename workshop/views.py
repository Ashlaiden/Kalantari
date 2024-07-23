from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from cart.models import Order
from product.models import Product
from tags.models import Branch


# Create your views here.
def home_page(request):
    branchs = Branch.manager.actives()
    context = {
        'branchs': branchs.reverse()
    }
    return render(request, 'workshop/home.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'workshop/product_list.html'
    paginate_by = 12

    def get_queryset(self):
        branch_name = self.kwargs.get('branch')
        try:
            branch = Branch.manager.actives().get(name=branch_name)
        except Branch.DoesNotExist:
            raise Http404("Category does not exist")
        return Product.published.get_by_branch(branch=branch)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branch'] = self.kwargs.get('branch')
        return context


class ProductWomanListView(ListView):
    template_name = 'workshop/product_list.html'
    paginate_by = 12

    def get_queryset(self):
        products = Product.published.all()
        if Product is not None:
            return products
        else:
            raise Http404("Product not found")

