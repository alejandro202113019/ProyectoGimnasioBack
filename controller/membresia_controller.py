# controller/membresia_controller.py
from flask import Blueprint, jsonify, request
from service.membresia_service import MembresiaService

membresia_blueprint = Blueprint('membresia', __name__)
membresia_service = MembresiaService()

@membresia_blueprint.route('/membresias', methods=['GET'])
def obtener_membresias():
    try:
        membresias = membresia_service.obtener_todos()
        return jsonify(membresias), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@membresia_blueprint.route('/membresias/<int:id_membresia>', methods=['GET'])
def obtener_membresia(id_membresia):
    try:
        membresia = membresia_service.obtener_por_id(id_membresia)
        if membresia:
            return jsonify(membresia), 200
        return jsonify({'error': 'Membresía no encontrada'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@membresia_blueprint.route('/membresias', methods=['POST'])
def crear_membresia():
    try:
        datos = request.get_json()
        mensaje = membresia_service.crear(datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@membresia_blueprint.route('/membresias/<int:id_membresia>', methods=['PUT'])
def actualizar_membresia(id_membresia):
    try:
        datos = request.get_json()
        mensaje = membresia_service.actualizar(id_membresia, datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@membresia_blueprint.route('/membresias/<int:id_membresia>', methods=['DELETE'])
def eliminar_membresia(id_membresia):
    try:
        mensaje = membresia_service.eliminar(id_membresia)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200
