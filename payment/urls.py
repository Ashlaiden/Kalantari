# Github.com/Rasooll
from django.urls import path
from .views import *

app_name = 'payment'

urlpatterns = [
    path('request/', send_request, name='request'),
    path('verify/', verify , name='verify'),
]


