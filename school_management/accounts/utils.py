import jwt
from django.conf import settings
from datetime import datetime, timedelta

JWT_SECRET = settings.SECRET_KEY
JWT_ALGORITHM = 'HS256'

def generate_jwt(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'role': user.profile.role,
        'exp': datetime.utcnow() + timedelta(hours=1),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decode_jwt(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None