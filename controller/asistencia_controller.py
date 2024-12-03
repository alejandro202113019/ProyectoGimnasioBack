# controller/asistencia_controller.py
from flask import Blueprint, jsonify, request
from service.asistencia_service import AsistenciaService

asistencia_blueprint = Blueprint('asistencia', __name__)
asistencia_service = AsistenciaService()

@asistencia_blueprint.route('/asistencias', methods=['GET'])
def obtener_asistencias():
    try:
        asistencias = asistencia_service.obtener_todos()
        return jsonify(asistencias), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@asistencia_blueprint.route('/asistencias/<int:id_cliente>', methods=['GET'])
def obtener_asistencia(id_cliente):
    try:
        asistencia = asistencia_service.obtener_por_id(id_cliente)
        if asistencia:
            return jsonify(asistencia), 200
        return jsonify({'error': 'Asistencia no encontrada'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200


@asistencia_blueprint.route('/asistencias', methods=['POST'])
def crear_asistencia():
    try:
        datos = request.get_json()
        mensaje = asistencia_service.crear(datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@asistencia_blueprint.route('/asistencias/<int:id_asistencia>', methods=['PUT'])
def actualizar_asistencia(id_asistencia):
    try:
        datos = request.get_json()
        mensaje = asistencia_service.actualizar(id_asistencia, datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@asistencia_blueprint.route('/asistencias/<int:id_asistencia>', methods=['DELETE'])
def eliminar_asistencia(id_asistencia):
    try:
        mensaje = asistencia_service.eliminar(id_asistencia)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

