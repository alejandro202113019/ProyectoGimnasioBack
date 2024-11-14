# controller/horario_controller.py
from flask import Blueprint, jsonify, request
from service.horario_service import HorarioService

horario_blueprint = Blueprint('horario', __name__)
horario_service = HorarioService()

@horario_blueprint.route('/horarios', methods=['GET'])
def obtener_horarios():
    try:
        horarios = horario_service.obtener_todos()
        return jsonify(horarios), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@horario_blueprint.route('/horarios/<int:id_horario>', methods=['GET'])
def obtener_horario(id_horario):
    try:
        horario = horario_service.obtener_por_id(id_horario)
        if horario:
            return jsonify(horario), 200
        return jsonify({'error': 'Horario no encontrado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@horario_blueprint.route('/horarios', methods=['POST'])
def crear_horario():
    try:
        datos = request.get_json()
        mensaje = horario_service.crear(datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@horario_blueprint.route('/horarios/<int:id_horario>', methods=['PUT'])
def actualizar_horario(id_horario):
    try:
        datos = request.get_json()
        mensaje = horario_service.actualizar(id_horario, datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@horario_blueprint.route('/horarios/<int:id_horario>', methods=['DELETE'])
def eliminar_horario(id_horario):
    try:
        mensaje = horario_service.eliminar(id_horario)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200
