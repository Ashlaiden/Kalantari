from django.urls import path
from .views import *

app_name = 'favorite'

urlpatterns = [
    path('bookmark/', book_mark, name='bookmark'),
]
