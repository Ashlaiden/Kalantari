from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

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

