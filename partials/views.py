import uuid

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from core.core.make_data_grouper import make_data_grouper
from cart.models import Order
from favorite.models import Favorite
from product.models import Product


# Create your views here.
def global_cookies(request):
    if request.user.is_authenticated:
        pass
        return JsonResponse({'status': True, 'session_uid': 'authenticated'})
        # items = Order.order_manager.get_order_items(request.user)
    else:
        session_uid = None
        try:
            if not request.session['u_id']:
                request.session['u_id'] = str(uuid.uuid4())
            session_uid = request.session['u_id']
        except KeyError:
            request.session['u_id'] = str(uuid.uuid4())
            session_uid = request.session['u_id']
        return JsonResponse({'status': True, 'session_uid': session_uid})


def account_user_menu(request):
    if request.user.is_authenticated:

        context = {
            'full_name': f'{request.user.first_name} {request.user.last_name}',
        }
        return render(request, 'partial/user-menu-account.html', context)
    else:
        context = {}
        return render(request, 'partial/user-menu-account-login.html', context)


def cart_user_menu(request):
    # if request.user.is_authenticated:
    #     items = Order.order_manager.get_order_items(request.user)
    # else:
    #     session_uid = None
    #     try:
    #         if not request.session['u_id']:
    #             request.session['u_id'] = str(uuid.uuid4())
    #         session_uid = request.session['u_id']
    #     except KeyError:
    #         request.session['u_id'] = str(uuid.uuid4())
    #         session_uid = request.session['u_id']
    #         items = Order.order_manager.get_order_items(request.user)
    print(request.session.get('u_id'))
    items = Order.order_manager.get_order_items(
        user=request.user if request.user.is_authenticated else None,
        session_uid=request.session.get('u_id') if not request.user.is_authenticated else None
    )
    price = 0
    for item in items if items is not None else []:
        price += (item.price * item.count)
    discount = 0
    final_price = price - discount
    context = {}
    if items:
        context = {
            'empty': False,
            'items': items,
            'price': price,
            'discount': discount,
            'final_price': final_price
        }
    else:
        context = {
            'empty': True,
            'items': items,
            'price': price,
            'discount': discount,
            'final_price': final_price
        }
    return render(request, 'partial/user-menu-cart.html', context)


# @login_required
def favorite_user_menu(request):
    is_authenticated = request.user.is_authenticated
    if is_authenticated:
        items = Favorite.manager.get_favorites(request.user)
    else:
        session_uid = None
        try:
            if not request.session['u_id']:
                request.session['u_id'] = str(uuid.uuid4())
            session_uid = request.session['u_id']
        except KeyError:
            request.session['u_id'] = str(uuid.uuid4())
            session_uid = request.session['u_id']
        items = Favorite.manager.get_favorites(session_uid=session_uid)
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
    return render(request, 'partial/user-menu-favorite.html', context)


def highest_score_products(request):
    products = Product.published.get_highest_score_products(count=8)
    # data = make_data_grouper(4, products)
    context = {
        'products': products
    }
    return render(request, 'partial/highest_score_products.html', context)


















