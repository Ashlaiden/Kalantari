from django.urls import path
from .views import *

app_name = 'favorite'

urlpatterns = [
    path('bookmark/', book_mark, name='bookmark'),
    path('_items_list/', favorite_items, name='favorite_items' )
]
