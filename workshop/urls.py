from django.urls import path
from .views import *

app_name = 'workshop'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('list/<str:branch>/', ProductListView.as_view(), name='product_list'),
    path('list/woman/', ProductWomanListView.as_view(), name='product_woman_list')
]


