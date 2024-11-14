# controller/equipo_controller.py
from flask import Blueprint, jsonify, request
from service.equipo_service import EquipoService

equipo_blueprint = Blueprint('equipo', __name__)
equipo_service = EquipoService()

@equipo_blueprint.route('/equipos', methods=['GET'])
def obtener_equipos():
    try:
        equipos = equipo_service.obtener_todos()
        return jsonify(equipos), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@equipo_blueprint.route('/equipos/<int:id_equipo>', methods=['GET'])
def obtener_equipo(id_equipo):
    try:
        equipo = equipo_service.obtener_por_id(id_equipo)
        if equipo:
            return jsonify(equipo), 200
        return jsonify({'error': 'Equipo no encontrado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@equipo_blueprint.route('/equipos', methods=['POST'])
def crear_equipo():
    try:
        datos = request.get_json()
        mensaje = equipo_service.crear(datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@equipo_blueprint.route('/equipos/<int:id_equipo>', methods=['PUT'])
def actualizar_equipo(id_equipo):
    try:
        datos = request.get_json()
        mensaje = equipo_service.actualizar(id_equipo, datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@equipo_blueprint.route('/equipos/<int:id_equipo>', methods=['DELETE'])
def eliminar_equipo(id_equipo):
    try:
        mensaje = equipo_service.eliminar(id_equipo)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200
