# from django.db import IntegrityError
# from django.http import JsonResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth import (
#     login,
#     logout,
#     get_user_model,
#     authenticate,
# )
# from django.contrib.auth.models import User
# from core.core.generator import generate_user_name
# from ..forms import *
# from ..models import Account
#
#
# def login_core(request):
#     if request.user.is_authenticated:
#         return JsonResponse({'code': '405', 'success': False, 'status': 'error', 'message': 'You are already logged in'})
#     login_form = LoginForm(request.POST or None)
#     if login_form.is_valid():
#         cd = login_form.cleaned_data
#         email = cd['email']
#         password = cd['passwd']
#         usr = authenticate(request, email=email, password=password)
#         if usr is not None:
#             login(request, usr)
#             return JsonResponse({'code': '200', 'success': True, 'status': 'ok', 'message': 'login success'})
#         else:
#             return JsonResponse({'code': '404', 'success': False, 'status': 'error', 'message': 'کاربری با این مشخصات یافت نشد!'})
#     if request.method != 'POST':
#         return JsonResponse({'code': '405', 'success': False, 'status': 'error', 'message': 'Invalid request'})
#     return JsonResponse({'code': '500', 'success': False, 'status': 'error', 'message': 'internal server error'})
#
#
# def create_account(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             return redirect('/')
#         register_form = RegisterForm(request.POST or None)
#         if register_form.is_valid():
#             cd = register_form.cleaned_data
#             if cd['privacy_accepted']:
#                 email = cd.get('email')
#                 passwd = cd.get('passwd')
#                 first_name = cd.get('first_name')
#                 last_name = cd.get('last_name')
#                 phone = cd.get('phone_number')
#                 gender = cd.get('gender')
#                 birth_date = cd.get('birth_date')
#                 try:
#                     Account.object.create_user(
#                         email=email,
#                         password=passwd,
#                         first_name=first_name,
#                         last_name=last_name,
#                         phone=phone,
#                         gender=gender,
#                         birth_date=birth_date
#                     )
#                     usr = authenticate(request, email=email, passwd=passwd)
#                     if usr is not None:
#                         login(request, usr)
#                         return redirect('/')
#                     else:
#                         return JsonResponse({'code': '404', 'success': False, 'status': 'error',
#                                             'message': 'کاربری با این مشخصات یافت نشد!'})
#                 except IntegrityError:
#                     return JsonResponse({'code': '500', 'success': False, 'status': 'error', 'message': 'internal server error'})
#
#     else:
#         return JsonResponse({'code': '405', 'success': False, 'status': 'error', 'message': 'Invalid request method'})
#
#
#
