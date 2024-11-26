from flask import Blueprint, request, jsonify
from utils.database import Database
from utils.auth import generar_token
import bcrypt

auth_blueprint = Blueprint('auth', __name__)
db = Database()

@auth_blueprint.route('/login', methods=['POST'])
def login_usuario():
    try:
        data = request.json
        user = data.get('user')
        password = data.get('password')

        # Validaciones
        if not user or not password:
            return jsonify({'status': False, 'message': 'Usuario y contraseña son obligatorios'}), 400

        # Obtener usuario de la tabla
        query = "SELECT `User`, `Password` FROM Login WHERE `User` = %s"
        usuario = db.execute_query(query, (user,), dictionary=True)

        if not usuario:
            return jsonify({'status': False, 'message': 'Credenciales inválidas'}), 401

        usuario = usuario[0]

        # Validar contraseña
        if not bcrypt.checkpw(password.encode('utf-8'), usuario['Password'].encode('utf-8')):
            return jsonify({'status': False, 'message': 'Credenciales inválidas'}), 401

        # Generar token JWT
        token = generar_token(usuario['User'])

        return jsonify({
            'status': True,
            'message': 'Inicio de sesión exitoso',
            'data': {
                'user': usuario['User'],
                'token': token
            }
        }), 200

    except Exception as e:
        return jsonify({'status': False, 'message': str(e)}), 500
