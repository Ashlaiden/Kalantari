from django.urls import path
from .views import *

app_name = 'workshop'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('list/man/', ProductManListView.as_view(), name='product_man_list'),
    path('list/woman/', ProductWomanListView.as_view(), name='product_woman_list')
]


