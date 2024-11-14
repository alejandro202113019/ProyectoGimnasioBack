# controller/clase_controller.py
from flask import Blueprint, jsonify, request
from service.clase_service import ClaseService

clase_blueprint = Blueprint('clase', __name__)
clase_service = ClaseService()

@clase_blueprint.route('/clases', methods=['GET'])
def obtener_clases():
    try:
        clases = clase_service.obtener_todos()
        return jsonify(clases), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@clase_blueprint.route('/clases/<int:id_clase>', methods=['GET'])
def obtener_clase(id_clase):
    try:
        clase = clase_service.obtener_por_id(id_clase)
        if clase:
            return jsonify(clase), 200
        return jsonify({'error': 'Clase no encontrada'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@clase_blueprint.route('/clases', methods=['POST'])
def crear_clase():
    try:
        datos = request.get_json()
        mensaje = clase_service.crear(datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@clase_blueprint.route('/clases/<int:id_clase>', methods=['PUT'])
def actualizar_clase(id_clase):
    try:
        datos = request.get_json()
        mensaje = clase_service.actualizar(id_clase, datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@clase_blueprint.route('/clases/<int:id_clase>', methods=['DELETE'])
def eliminar_clase(id_clase):
    try:
        mensaje = clase_service.eliminar(id_clase)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200
