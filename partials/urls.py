from django.urls import path
from .views import *

app_name = 'render_partials'

urlpatterns = [
    path('global-cookies/', global_cookies, name='global_cookies'),
    path('_user-menu/_account-section', account_user_menu, name='partial-user-menu-account-section'),
    path('_user-menu/_cart-section', cart_user_menu, name='partial-user-menu-cart-section'),
    path('_user-menu/_favorite-section', favorite_user_menu, name='partial-user-menu-favorite-section'),
    path('most/_score/', highest_score_products, name='partial-most-score-products')
]

