from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('', user_dashboard, name='user_dashboard'),
    path('<path:sub_path>/', user_dashboard, name='user_dashboard_with_sub_path'),
]


