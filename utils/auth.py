import jwt
import datetime
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

JWT_SECRET = os.getenv('JWT_SECRET', 'secret_key_default')
JWT_ALGORITHM = 'HS256'

def generar_token(user):
    """Generar un token JWT para el usuario."""
    payload = {
        'user': user,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def token_requerido(f):
    """Decorador para proteger rutas con JWT."""
    @wraps(f)
    def decorador(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'status': False, 'message': 'Token no proporcionado'}), 401

        try:
            datos = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            request.user = datos['user']
        except jwt.ExpiredSignatureError:
            return jsonify({'status': False, 'message': 'El token ha expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'status': False, 'message': 'Token inválido'}), 401

        return f(*args, **kwargs)
    return decorador