from django.utils.deprecation import MiddlewareMixin
from .utils import decode_jwt
from django.contrib.auth.models import User

class JWTAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.COOKIES.get('jwt_token')
        if token:
            data = decode_jwt(token)
            if data:
                try:
                    request.user = User.objects.get(id=data['user_id'])
                    request.user.role = data['role']
                except User.DoesNotExist:
                    pass