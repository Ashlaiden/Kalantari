import uuid

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from cart.models import OrderItem
from favorite.models import Favorite
from .models import Product, ProductGallery, ProductView

from core.core.request_info import get_user_IP


# Create your views here.
def product_pk(request, uid):
    product = Product.published.get_by_uid(uid)
    product_uid = str(uid).replace('{', '').replace('}', '')
    product_slug = str(product.slug)
    url = reverse_lazy('product:product_detail', args=[product_uid, product_slug])
    return redirect(url)


def product_detail(request, uid, slug):
    product = Product.published.get_product(uid, slug=slug)
    ProductView.view_manager.add_product_view(
        ip_address=get_user_IP(request),
        user_id=request.user.id if request.user.is_authenticated else None,
        product_uid=product.uid



    )
    in_cart = OrderItem.order_detail_manager.is_exist(
        user=request.user if request.user.is_authenticated else None,
        session_uid=request.session.get('u_id') if not request.user.is_authenticated else None,
        product_uid=product.uid
    )
    if request.user.is_authenticated:
        in_favorite = Favorite.manager.is_in_favorites(product_uid=product.uid, user=request.user)
    else:
        session_uid = None
        try:
            if not request.session['u_id']:
                request.session['u_id'] = str(uuid.uuid4())
            session_uid = request.session['u_id']
        except KeyError:
            request.session['u_id'] = str(uuid.uuid4())
            session_uid = request.session['u_id']
        in_favorite = Favorite.manager.is_in_favorites(session_uid=session_uid, product_uid=product.uid)
    if in_cart:
        count = OrderItem.order_detail_manager.get_count(
            user=request.user if request.user.is_authenticated else None,
            session_uid=request.session.get('u_id') if not request.user.is_authenticated else None,
            product=product
        )
        full = False
        first = False
        if count == product.stock:
            full = True
        if count == 1:
            first = True
        context = {
            'product': product,
            'in_cart': in_cart,
            'count': count,
            'max': full,
            'first': first,
            'in_favorite': in_favorite
        }
        return render(request, 'product/product_detail.html', context)
    else:
        context = {
            'product': product,
            'in_cart': in_cart,
            'in_favorite': in_favorite
        }
        return render(request, 'product/product_detail.html', context)
