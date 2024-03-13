from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cart.models import Order


# Create your views here.
@login_required
def cart_user_menu(request):
    items = Order.order_manager.get_order_items(request.user)
    context = {}
    if items:
        context = {
            'empty': False,
            'items': items
        }
    else:
        context = {
            'empty': True,
            'items': items
        }
    return render(request, 'partial/user-menu-cart.html', context)


