from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('item/add/', add_item, name='add_item'),
    path('item/delete/', delete_item, name='delete_item'),
    path('change/count/', change_item_count, name='change_item_count'),
    path('order/info/', get_order_info, name='get_order_info'),
    path('_continue_ordering/', continue_ordering, name='continue_ordering'),
    path('_addressing_package/', addressing_package, name='addressing_package'),
    path('_addressing/_add_address/', add_address, name='add_address'),
    path('_addressing/_delete_address/', delete_address, name='delete_address'),
    path('_check_cart_items/', check_cart_items, name='check_cart_items'),
    path('_receipt/', receipt, name='receipt'),
]

