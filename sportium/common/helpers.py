from django.contrib.auth import get_user_model
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


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'
