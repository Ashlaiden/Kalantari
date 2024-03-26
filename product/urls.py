from django.urls import path
from .views import *


app_name = 'product'

urlpatterns = [
    path('<int:uid>/', product_pk, name='product_pk_detail'),
    path('<int:uid>/<slug>/', product_detail, name='product_detail')
]


