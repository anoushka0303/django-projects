from django.http import HttpResponseForbidden

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if hasattr(request.user, 'profile') and request.user.profile.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You don't have permission.")
        return wrapper
    return decorator