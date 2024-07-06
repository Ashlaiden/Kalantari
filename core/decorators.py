from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings
from functools import wraps


def login_required_redirect(next_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                login_url = settings.LOGIN_URL
                redirect_path = next_url if next_url else request.get_full_path()
                return redirect(f"{login_url}?next={redirect_path}")
            return view_func(request, *args, **kwargs)
        return login_required(_wrapped_view)
    return decorator
