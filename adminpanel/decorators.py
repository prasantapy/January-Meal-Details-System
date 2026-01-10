from django.shortcuts import redirect
from django.contrib import messages

def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        return redirect('admin_login')
    return wrapper
