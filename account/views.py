from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import (
    login,
    logout,
    get_user_model,
    authenticate,
)
from core.core.request_info import get_user_IP
from django.contrib.auth.models import User
from core.core.generator import generate_user_name
from favorite.models import Favorite
from .forms import *
from .models import Account
from cart.models import Order, OrderItem
import jdatetime

def login_user(request):
    next_url = request.build_absolute_uri(request.GET.get('next', '/')) if request.GET.get('next', '/') is not None else None
    print(f'next3: {next_url}')
    if request.method == 'POST':
        session_id = request.session.get('u_id')
        next_url = request.build_absolute_uri(request.POST.get('next')) if request.POST.get('next') is not None and next_url is None else next_url
        print(f'next4: {next_url}')
        if request.user.is_authenticated:
            return JsonResponse({'code': '405', 'success': False, 'status': 'error', 'message': 'You are already logged in', 'next': next_url})
        login_form = LoginForm(request.POST or None)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('passwd')
            usr = authenticate(request, email=email, password=password)
            if usr is not None:
                ip_address = get_user_IP(request)
                if ip_address is not None:
                    usr.last_IP = ip_address
                    usr.save()
                login(request, usr)

                order_user = Order.order_manager.get_active_order(user=request.user)
                order_session = Order.order_manager.get_active_order(session_uid=session_id)
                order_session_items = Order.order_manager.get_order_items(session_uid=session_id) if order_session is not None else None
                for item in order_session_items if order_session_items is not None else []:
                    in_cart = OrderItem.order_detail_manager.is_exist(user=request.user, product_uid=item.product.uid)
                    if in_cart:
                        item.delete()
                        continue
                    item.order = order_user
                    item.save()
                order_session.delete()

                favorites = Favorite.manager.get_favorites(session_uid=session_id)
                for item in favorites if favorites is not None else []:
                    in_favorite = Favorite.manager.is_in_favorites(product_uid=item.product.uid, user=request.user) or None
                    if in_favorite:
                        item.delete()
                        continue
                    item.user = request.user
                    item.session_uid = None
                    item.save()
                print(f'next2: {next_url}')
                return JsonResponse({'code': '200', 'success': True, 'status': 'ok', 'message': 'login success', 'next': next_url})
            else:
                return JsonResponse({'code': '404', 'success': False, 'status': 'error', 'message': 'کاربری با این مشخصات یافت نشد!', 'next': None})
        if request.method != 'POST':
            return JsonResponse({'code': '405', 'success': False, 'status': 'error', 'message': 'Invalid request', 'next': None})
        return JsonResponse({'code': '500', 'success': False, 'status': 'error', 'message': 'internal server error', 'next': None})
    else:
        next_url = request.build_absolute_uri(request.GET.get('next', '/')) if request.GET.get('next', '/') is not None and next_url is None else next_url
        print(f'next1: {next_url}')
        if request.user.is_authenticated:
            return redirect(next_url if next_url is not None else '/')
        else:
            context = {

            }
            return render(request, 'account/login.html', context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'code': '200', 'success': True, 'status': 'ok', 'message': 'logout success'})
    else:
        return JsonResponse({'code': '404', 'success': False, 'status': 'error', 'message': 'user not found'})


def register_account(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return JsonResponse({'code': '405', 'success': False, 'status': 'error', 'message': 'Invalid request'})
        register_form = RegisterForm(request.POST or None)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            if cd['privacy_accepted']:
                email = cd.get('email')
                passwd = cd.get('passwd')
                first_name = cd.get('first_name')
                last_name = cd.get('last_name')
                phone = cd.get('phone_number')
                gender = cd.get('gender')
                if cd.get('birth_date'):
                    birth_date = cd.get('birth_date')
                else:
                    birth_date = None
                try:
                    if birth_date is not None:
                        Account.object.create_user(
                            email=email,
                            password=passwd,
                            first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            gender=gender,
                            birth_date=birth_date,
                            is_active=True,
                            is_staff=False
                        )
                    else:
                        Account.object.create_user(
                            email=email,
                            password=passwd,
                            first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            gender=gender,
                            is_active=True,
                            is_staff=False
                        )
                    usr = authenticate(request, email=email, password=passwd)
                    if usr is not None:
                        Order.object.create(user=usr)
                        login(request, usr)
                        return JsonResponse({'code': '200', 'success': True, 'status': 'ok', 'message': 'account creation success'})
                    else:
                        return JsonResponse({'code': '404', 'success': False, 'status': 'error',
                                            'message': 'کاربری با این مشخصات یافت نشد!'})
                except IntegrityError:
                    return JsonResponse({'code': '500', 'success': False, 'status': 'error', 'message': 'internal server error', 'error': cd.get('error'), 'user': 'user didn\tt created'})
            else:
                return JsonResponse({'code': '500', 'success': False, 'status': 'error', 'message': 'internal server error', 'error': cd.get('error')})
        else:
            return JsonResponse({'code': '500', 'success': False, 'status': 'error', 'message': 'internal server error', 'error': 'form is not valid', 'form': register_form.errors})
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            context = {

            }
            return render(request, 'account/register.html', context)


def is_authenticated(request):
    if request.user.is_authenticated:
        return JsonResponse({'code': '200', 'success': 1, 'authenticated': 1})
    else:
        return JsonResponse({'code': '200', 'success': 1, 'authenticated': 0})


def profile_dashboard(request):
    if request.method == 'POST':
        pass
    else:
        if request.user.is_authenticated:
            account: Account = request.account
            context = {
                'full_name': f'{request.user.first_name} {request.user.last_name}',
                'email_address': f'{request.user.email}',
                'email_confirmed': False,
                'last_login': jdatetime.datetime.fromgregorian(datetime=account.last_login).strftime("%Y/%m/%d - %H:%M"),
                'last_ip': account.last_IP,
            }
        else:
            context = {}
        return render(request, 'dashboard/profile-component.html', context)









