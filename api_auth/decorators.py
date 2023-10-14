from functools import wraps
from rest_framework.response import Response


def is_hr(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.group == 'HR':
            return view_func(request, *args, **kwargs)
        else:
            return Response({"detail": "Access denied. HR Only."}, status=403)

    return _wrapped_view
