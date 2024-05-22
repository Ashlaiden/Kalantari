from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('item/add/', add_item, name='add_item'),
    path('item/delete/', delete_item, name='delete_item'),
    path('change/count/', change_item_count, name='change_item_count'),
    path('order/info/', get_order_info, name='get_order_info')
]

