from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
@login_required
def cart(request):
    if request.method == "POST":
        pass
    else:
        context = {
            
        }
        return render(request, 'cart/cart.html', context)
