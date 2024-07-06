from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_account, name='register'),
    path('_authenticated/', is_authenticated, name='is_authenticated')
]

