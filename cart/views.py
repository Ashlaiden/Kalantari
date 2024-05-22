from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
# @login_required
def cart(request):
    if request.method == "POST":
        pass
    else:
        # order = Order.order_manager.get_active_order(request.user)
        # items = OrderItem.order_detail_manager.get_by_order(order)
        # data = []
        items = Order.order_manager.get_order_items(
            user=request.user if request.user.is_authenticated else None,
            session_uid=request.session.get('u_id') if not request.user.is_authenticated else None
        )
        # for item in items:
        #     full = False
        #     if item.count == item.product.stock:
        #         full = True
        #     asset = {'item': item, 'max': full}
        #     data.append(asset)
        context = {
            'items': items
        }
        return render(request, 'cart/cart.html', context)


# @login_required
def change_item_count(request):
    if request.method == "POST":
        fd = ChangeCount(request.POST or None)
        if fd.is_valid():
            cd = fd.cleaned_data
            uid = cd['uid']
            action = cd['action']
            item: OrderItem = OrderItem.order_detail_manager.get_detail(
                user=request.user if request.user.is_authenticated else None,
                session_uid=request.session.get('u_id') if not request.user.is_authenticated else None,
                uid=uid,
                product_uid=uid
            )
            if item is not None:
                if action == '+':
                    if item.count == item.product.stock:
                        return JsonResponse({'status': 'error', 'message': 'you already have maximum count in stock!'})
                    else:
                        item.count += 1
                elif action == '-':
                    if item.count == 1:
                        return JsonResponse({'status': 'error', 'message': 'Count should be one or bigger!'})
                    else:
                        item.count -= 1
                else:
                    return JsonResponse({'status': 'error', 'message': 'Invalid Data'})
                    # return JsonResponse({'code': '405', 'success': False, 'status': 'error', 'message': 'Invalid request'})
                item.save()
                detail = {
                    'uid': item.uid
                }
                if item.count == item.product.stock:
                    return JsonResponse({'status': 'ok', 'count': item.count, 'max': 'true', 'detail': detail})
                else:
                    return JsonResponse({'status': 'ok', 'count': item.count, 'max': 'false', 'detail': detail})
            else:
                return JsonResponse({'status': 'error', 'message': 'Not Found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data is not valid'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid Request'})


# @login_required
def delete_item(request):
    if request.method == "POST":
        fd = DeleteItem(request.POST or None)
        if fd.is_valid():
            cd = fd.cleaned_data
            uid = cd['uid']
            item: OrderItem = OrderItem.order_detail_manager.get_detail(
                user=request.user if request.user.is_authenticated else None,
                session_uid=request.session.get('u_id') if not request.user.is_authenticated else None,
                uid=uid,
                product_uid=uid
            )
            if item is not None:
                item_uid = item.uid
                item.delete()
                detail = {
                    'uid': item_uid
                }
                return JsonResponse({'status': 'ok', 'detail': detail})
            else:
                return JsonResponse({'status': 'error', 'message': 'Not Found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data is not valid'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid Request'})


# @login_required
def add_item(request):
    if request.method == "POST":
        fd = AddItem(request.POST or None)
        if fd.is_valid():
            cd = fd.cleaned_data
            uid = cd['uid']
            order = Order.order_manager.get_active_order(
                user=request.user if request.user.is_authenticated else None,
                session_uid=request.session.get('u_id') if not request.user.is_authenticated else None
            )
            if order is None:
                order = Order.order_manager.create(
                    user=request.user if request.user.is_authenticated else None,
                    session_uid=request.session.get('u_id') if not request.user.is_authenticated else None,
                    is_paid=False
                )
            if OrderItem.order_detail_manager.is_exist(user=request.user if request.user.is_authenticated else None, session_uid=request.session.get('u_id') if not request.user.is_authenticated else None, product_uid=uid) is False:
                product = Product.published.get_by_uid(uid=uid)
                print(f'order: {order}')
                OrderItem.order_detail_manager.create(order=order, product=product, price=product.price, count=1)
                detail_obj = OrderItem.order_detail_manager.get_detail(
                    user=request.user if request.user.is_authenticated else None,
                    session_uid=request.session.get('u_id') if not request.user.is_authenticated else None,
                    product=product
                )
                print(f"items: {Order.order_manager.get_order_items(session_uid=request.session.get('u_id'))}")
                print(detail_obj)
                detail = {
                    'uid': detail_obj.uid,
                    'image_url': detail_obj.product.cover_image.url,
                    'title': detail_obj.product.title,
                    'price': detail_obj.price,
                    'count': detail_obj.count,
                    'product_url': detail_obj.product.get_absolute_url()
                }
                if product.stock == 1:
                    return JsonResponse({'status': 'ok', 'max': 'true', 'detail': detail})
                else:
                    return JsonResponse({'status': 'ok', 'max': 'false', 'detail': detail})
            else:
                return JsonResponse({'status': 'error', 'message': 'Already Exist in Order!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data is not valid'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid Request'})


# @login_required
def get_order_info(request):
    order = Order.order_manager.get_active_order(
        user=request.user if request.user.is_authenticated else None,
        session_uid=request.session.get('u_id') if not request.user.is_authenticated else None
    )
    details = OrderItem.order_detail_manager.get_by_order(
        user=request.user if request.user.is_authenticated else None,
        session_uid=request.session.get('u_id') if not request.user.is_authenticated else None,
        order=order
    )
    price = 0
    for item in details:
        price += (item.price * item.count)
    discount = 0
    final_price = price - discount
    return JsonResponse({'status': 'od', 'price': price, 'discount': discount, 'final_price': final_price})





















    6