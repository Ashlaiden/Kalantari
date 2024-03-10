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
from .forms import *
from .models import Account
from cart.models import Order


def login_user(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return JsonResponse({'code': '405', 'success': False, 'status': 'error', 'message': 'You are already logged in'})
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
                return JsonResponse({'code': '200', 'success': True, 'status': 'ok', 'message': 'login success'})
            else:
                return JsonResponse({'code': '404', 'success': False, 'status': 'error', 'message': 'کاربری با این مشخصات یافت نشد!'})
        if request.method != 'POST':
            return JsonResponse({'code': '405', 'success': False, 'status': 'error', 'message': 'Invalid request'})
        return JsonResponse({'code': '500', 'success': False, 'status': 'error', 'message': 'internal server error'})
    else:
        if request.user.is_authenticated:
            return redirect('/')
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














