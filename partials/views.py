import uuid

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from cart.models import Order
from favorite.models import Favorite


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



