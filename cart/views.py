import json
from datetime import datetime, timedelta
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from account.models import Address
from core.decorators import login_required_redirect
from .models import *
from .forms import *


# Create your views here.
# @login_required
def cart(request):
    if request.method == "POST":
        return JsonResponse({'status': 'error', 'success': 0, 'message': 'Invalid Request!'})
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
        order_info = json.loads(get_order_info(request).content.decode())

        info = {
            'price': order_info['price'],
            'discount': order_info['discount'],
            'tax': order_info['tax'],
            'final_price': order_info['final_price']
        }
        context = {
            'items': items,
            'info': info
        }
        return render(request, 'cart/cart-component.html', context)


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
                or_bj = Order.order_manager.get_active_order(user=request.user)
                or_bj.updated = timezone.now()
                or_bj.save()
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
                or_bj = Order.order_manager.get_active_order(user=request.user)
                or_bj.updated = timezone.now()
                or_bj.save()
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
            if OrderItem.order_detail_manager.is_exist(user=request.user if request.user.is_authenticated else None,
                                                       session_uid=request.session.get(
                                                               'u_id') if not request.user.is_authenticated else None,
                                                       product_uid=uid) is False:
                product = Product.published.get_by_uid(uid=uid)
                OrderItem.order_detail_manager.create(order=order, product=product, price=product.price, count=1)
                detail_obj = OrderItem.order_detail_manager.get_detail(
                    user=request.user if request.user.is_authenticated else None,
                    session_uid=request.session.get('u_id') if not request.user.is_authenticated else None,
                    product=product
                )
                detail = {
                    'uid': detail_obj.uid,
                    'image_url': detail_obj.product.cover_image.url,
                    'title': detail_obj.product.title,
                    'price': detail_obj.price,
                    'count': detail_obj.count,
                    'product_url': detail_obj.product.get_absolute_url()
                }
                or_bj = Order.order_manager.get_active_order(user=request.user)
                or_bj.updated = timezone.now()
                or_bj.save()
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
    order.updated = timezone.now()
    order.save()
    details = OrderItem.order_detail_manager.get_by_order(
        user=request.user if request.user.is_authenticated else None,
        session_uid=request.session.get('u_id') if not request.user.is_authenticated else None,
        order=order
    )
    singles_price = 0
    singles_tax = 0
    price = 0
    for item in details:
        price += (item.price * item.count)
        singles_price += item.price
        singles_tax += ((item.price / 100) * 9)
    discount = 0
    final_price = price - discount
    tax = int((final_price / 100) * 9)
    final_price += tax
    return JsonResponse(
        {
            'status': 'od',
            'price': f"{price:,}",
            'discount': f"{discount:,}",
            'tax': f"{tax:,}",
            'final_price': f"{final_price:,}",
            'single_price_sum': f"{singles_price:,}",
            'single_tax_sum': f"{singles_tax:,}",
            'price_discount': f"{(price - discount):,}",

        }
    )


@csrf_exempt
@login_required_redirect(next_url='/dashboard/cart/order/')
def continue_ordering(request):
    if request.method == 'POST':
        order: Order = Order.order_manager.get_active_order(user=request.user)

        match order.step:
            case 'OP':
                order.step = order.STEP.ADDRESSING
            case 'AD':
                order.step = order.STEP.ADDRESSING
            case 'CO':
                order.step = order.STEP.ADDRESSING
            case 'RC':
                order.step = order.STEP.CHECKOUT
            case 'PA':
                order.step = order.STEP.RECEIPT
            case 'CA':
                order.step = order.STEP.PAYMENT
            case 'ER':
                order.step = order.STEP.PAYMENT
            case _:
                order.step = order.STEP.ADDRESSING
        order.save()
        data = {
            'status': 'ok',
            'success': 1,
            'step': order.step,
        }
        return JsonResponse(data)
    elif request.method == 'GET':
        order: Order = Order.order_manager.get_active_order(user=request.user)
        time_difference = timezone.now() - order.updated
        if time_difference > timedelta(minutes=5):
            order.step = order.STEP.ADDRESSING
            order.step_updated = timezone.now()
            order.save()
            step = order.step
        else:
            step = order.step
        context = {}
        data = {
            'status': 'ok',
            'success': 1,
            'content': render_to_string('cart/continue_order_main.html', context),
            'step': step,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'status': 'error', 'code': 400})


@login_required_redirect(next_url='/dashboard/cart/order/addressing/')
def addressing_package(request):
    if request.method == 'POST':
        fd = FinalizedAddress(request.POST or None)
        if fd.is_valid():
            cd = fd.cleaned_data
            addr_id = cd['id']
            order: Order = Order.order_manager.get_active_order(user=request.user)
            # addr: Address = Address.address_manager.get_address(item_id=addr_id, user=request.user)
            addr = Address.address_manager.get_queryset().get(pk=addr_id)

            order.address = addr
            order.address_finalized = addr.address

            order.step = order.STEP.CHECKOUT
            order.step_updated = timezone.now()
            order.save()

            return JsonResponse({'status': 'ok', 'success': 1, 'step': order.step})
        else:
            return JsonResponse({'status': 'error', 'success': 0})
    elif request.method == 'GET':
        order: Order = Order.order_manager.get_active_order(user=request.user)
        order.step = order.STEP.ADDRESSING
        order.save()
        addresses = Address.address_manager.get_user_addresses(user=request.user)

        print(f'Addresses: {addresses}')

        context = {
            'address_items': addresses,
        }
        return render(request, 'cart/addressing_package.html', context)
    else:
        return JsonResponse({'status': 'error', 'code': 400})


@login_required_redirect(next_url='/dashboard/cart/order/addressing/')
def add_address(request):
    if request.method == 'POST':
        fd = AddAddress(request.POST or None)
        if fd.is_valid():
            cd = fd.cleaned_data
            title = cd['title']
            address = cd['address']
            if Address.address_manager.get_user_address_count(user_id=request.user.id) <= 4:
                if not Address.address_manager.unique_address_title(title, user_id=request.user.id):
                    return JsonResponse({'status': 'error', 'success': 0, 'code': 3})
                new_address = Address.address_manager.create(title=title, address=address, user=request.user)
                new_address.save()
                temp = {
                    'title': new_address.title,
                    'date': new_address.j_created.strftime("%Y/%m/%d"),
                    'address': new_address.address,
                    'id': new_address.id
                }
                return JsonResponse({'status': 'ok', 'success': 1, 'code': 1, 'content': temp})
            else:
                return JsonResponse({'status': 'error', 'success': 0, 'code': 5})
        else:
            return JsonResponse({'status': 'error', 'success': 0})
    else:
        return JsonResponse({'status': 'error', 'success': 0})


@login_required_redirect(next_url='/dashboard/cart/order/addressing/')
def delete_address(request):
    if request.method == 'POST':
        fd = EditOrDeleteAddress(request.POST or None)
        if fd.is_valid():
            try:
                cd = fd.cleaned_data
                item_id = cd['id']
                address_obj: Address = Address.address_manager.get_address(item_id=item_id, user=request.user)
                address_obj.delete()
                return JsonResponse({'status': 'ok', 'success': 1})
            except BaseException:
                return JsonResponse({'status': 'error', 'success': 0})
            # edit_flag = cd['edit_flag'] if cd['edit_flag'] is not None else None
            # delete_flag = cd['delete_flag'] if cd['delete_flag'] is not None else None
            # title = cd['title'] if cd['title'] is not None else None
            # address = cd['address'] if cd['address'] is not None else None
            # if edit_flag and item_id is not None:
            #     if not Address.address_manager.unique_address_title(title, user_id=request.user.id):
            #         return JsonResponse({'status': 'error', 'success': 0, 'code': 3})
            #     address_obj: Address = Address.address_manager.get_address(item_id=item_id, user=request.user)
            #     address_obj.title = title
            #     address_obj.address = address
            #     address_obj.save()
            #     temp = {
            #         'title': address_obj.title,
            #         'date': address_obj.j_created.strftime("%d/%m/%Y"),
            #         'address': address_obj.address,
            #         'id': address_obj.id
            #     }
            #     return JsonResponse({'status': 'ok', 'success': 1, 'code': 1, 'content': temp})
            # elif delete_flag and item_id is not None:
            #     address_obj: Address = Address.address_manager.get_address(item_id=item_id, user=request.user)
            #     address_obj.delete()
            #     return JsonResponse({'status': 'ok', 'success': 1, 'code': 1})
            # else:
            #     return JsonResponse({'status': 'error', 'success': 0, 'code': 5})
        else:
            return JsonResponse({'status': 'error', 'success': 0})
    else:
        return JsonResponse({'status': 'error', 'success': 0})


@login_required_redirect(next_url='/dashboard/cart/order/checkout/')
def check_cart_items(request):
    if request.method == 'POST':
        fd = FinalizedCheckout(request.POST or None)
        if fd.is_valid():
            cd = fd.cleaned_data
            accepted = cd['accept']
            if accepted:
                order: Order = Order.order_manager.get_active_order(user=request.user)
                if order.step == 'CO':
                    order.step = order.STEP.RECEIPT
                    order.step_updated = timezone.now()
                    order.save()
                    return JsonResponse({'status': 'ok', 'success': 1, 'step': order.step})
                else:
                    return JsonResponse({'status': 'error', 'success': 0})
            else:
                return JsonResponse({'status': 'error', 'success': 0})
        else:
            return JsonResponse({'status': 'error', 'success': 0})
    elif request.method == 'GET':
        items = Order.order_manager.get_order_items(user=request.user)
        order_info = json.loads(get_order_info(request).content.decode())
        info = {
            'price': order_info['price'],
            'discount': order_info['discount'],
            'tax': order_info['tax'],
            'final_price': order_info['final_price'],
            'items_count': items.count(),
        }
        context = {
            'items': items,
            'info': info,
        }
        return render(request, 'cart/check_cart_items.html', context)
    else:
        return JsonResponse({'status': 'error', 'code': 400})


@login_required_redirect(next_url='/dashboard/cart/order/receipt/')
def receipt(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        order: Order = Order.order_manager.get_active_order(user=request.user)
        items = Order.order_manager.get_order_items(user=request.user)
        order_info = json.loads(get_order_info(request).content.decode())
        date = timezone.now().strftime("%Y/%m/%d")
        info = {
            'price': order_info['price'],
            'discount': order_info['discount'],
            'tax': order_info['tax'],
            'final_price': order_info['final_price'],
            'single_price': order_info['single_price_sum'],
            'price_discount': order_info['price_discount'],
            'items_count': items.count(),
        }
        context = {
            'order': order,
            'items': items,
            'info': info,
            'date': date,
        }
        return render(request, 'cart/receipt.html', context)
    else:
        return JsonResponse({'status': 'error', 'code': 400})
