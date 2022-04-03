from django.shortcuts import redirect


class RedirectToHomeMixin:
    # here we put the logic if a user is logged in to redirect to dashboard
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)
