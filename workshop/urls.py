from django.urls import path
from .views import *

app_name = 'workshop'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('<category>/', ProductListView.as_view(), name='product_list')
]


