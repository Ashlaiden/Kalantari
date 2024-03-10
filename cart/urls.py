from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('change/count/', change_item_count, name='change_item_count'),
    path('delete/item/', delete_item, name='delete_item')
]

