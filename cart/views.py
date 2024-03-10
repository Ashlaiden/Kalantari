from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
@login_required
def cart(request):
    if request.method == "POST":
        pass
    else:
        # order = Order.order_manager.get_active_order(request.user)
        # items = OrderItem.order_detail_manager.get_by_order(order)
        items = Order.order_manager.get_order_items(request.user)
        context = {
            'items': items
        }
        return render(request, 'cart/cart.html', context)


@login_required
def change_item_count(request):
    if request.method == "POST":
        fd = ChangeCount(request.POST or None)
        if fd.is_valid():
            cd = fd.cleaned_data
            uid = cd['uid']
            action = cd['action']
            item: OrderItem = OrderItem.order_detail_manager.get_detail(user=request.user, detail_uid=uid)
            if item is not None:
                if action == '+':
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
                return JsonResponse({'status': 'ok', 'count': item.count})
            else:
                return JsonResponse({'status': 'error', 'message': 'Not Found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data is not valid'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid Request'})


@login_required
def delete_item(request):
    if request.method == "POST":
        fd = DeleteItem(request.POST or None)
        if fd.is_valid():
            cd = fd.cleaned_data
            uid = cd['uid']
            item: OrderItem = OrderItem.order_detail_manager.get_detail(user=request.user, detail_uid=uid)
            if item is not None:
                item.delete()
                return JsonResponse({'status': 'ok'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Not Found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Data is not valid'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid Request'})

