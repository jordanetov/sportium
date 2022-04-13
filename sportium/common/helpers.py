from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect

UserModel: object = get_user_model()


def needed_permission(permission):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated or not user.has_perms(permission):
                return redirect('no permission')
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
