from django.urls import path
from .views import *

app_name = 'render_partials'

urlpatterns = [
    path('global-cookies/', global_cookies, name='global_cookies'),
    path('user-menu/cart-section', cart_user_menu, name='partial-user-menu-cart-section'),
]

