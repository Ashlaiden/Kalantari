import uuid

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from cart.models import OrderItem
from product.models import Product
from .models import Favorite
from .forms import *


# Create your views here.
def book_mark(request):
    if request.method == 'POST':
        fd = BookMarkForm(request.POST or None)
        if fd.is_valid():
            cd = fd.cleaned_data
            uid = cd['uid']
            if request.user.is_authenticated:
                if Favorite.manager.is_in_favorites(user=request.user, product_uid=uid):
                    Favorite.manager.get_favorite(user=request.user, product_uid=uid).delete()
                    return JsonResponse({'status': 'ok', 'message': 'removed'})
                else:
                    product = Product.published.get_by_uid(uid=uid)
                    Favorite.object.create(user=request.user, product=product)
                    detail = {
                        'uid': product.uid,
                        'image_url': product.cover_image.url,
                        'title': product.title,
                        'product_url': product.get_absolute_url()
                    }
                    return JsonResponse({'status': 'ok', 'message': 'added', 'detail': detail})
            else:
                if Favorite.manager.is_in_favorites(session_uid=request.session['u_id'], product_uid=uid):
                    Favorite.manager.get_favorite(session_uid=request.session['u_id'], product_uid=uid).delete()
                    return JsonResponse({'status': 'ok', 'message': 'removed'})
                else:
                    product = Product.published.get_by_uid(uid=uid)
                    Favorite.object.create(session_uid=request.session['u_id'], product=product)
                    detail = {
                        'uid': product.uid,
                        'image_url': product.cover_image.url,
                        'title': product.title,
                        'product_url': product.get_absolute_url()
                    }
                    return JsonResponse({'status': 'ok', 'message': 'added', 'detail': detail})
        else:
            return JsonResponse({'status': 'error', 'message': 'form is not valid'})
    else:
        return JsonResponse({'status': 'error', 'message': 'bad request'})


def favorite_items(request):
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
    data = list()
    for item in items:
        d = dict()
        d['item'] = item
        in_cart = OrderItem.order_detail_manager.is_exist(
            user=request.user if request.user.is_authenticated else None,
            session_uid=request.session.get('u_id') if not request.user.is_authenticated else None,
            product_uid=item.product.uid
        )
        if in_cart:
            d['in_cart'] = True
        else:
            d['in_cart'] = False
        data.append(d)
    context = {}
    if items:
        context = {
            'empty': False,
            'items': data
        }
    else:
        context = {
            'empty': True,
            'items': data
        }
    return render(request, 'dashboard/favorite-component.html', context)
