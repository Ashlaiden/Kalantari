from .models import Account


class AccountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.account = Account.object.get(id=request.user.id)
        else:
            request.account = None
        response = self.get_response(request)
        return response


