from flask import Blueprint, jsonify, request
from service.gasto_service import GastoService

gasto_blueprint = Blueprint('gasto', __name__)
gasto_service = GastoService()

@gasto_blueprint.route('/gastos', methods=['GET'])
def obtener_gastos():
    try:
        gastos = gasto_service.obtener_todos()
        return jsonify(gastos), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@gasto_blueprint.route('/gastos/<int:id_gasto>', methods=['GET'])
def obtener_gasto(id_gasto):
    try:
        gasto = gasto_service.obtener_por_id(id_gasto)
        if gasto:
            return jsonify(gasto), 200
        return jsonify({'error': 'Gasto no encontrado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@gasto_blueprint.route('/gastos', methods=['POST'])
def crear_gasto():
    try:
        datos = request.get_json()
        mensaje = gasto_service.crear(datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@gasto_blueprint.route('/gastos/<int:id_gasto>', methods=['PUT'])
def actualizar_gasto(id_gasto):
    try:
        datos = request.get_json()
        mensaje = gasto_service.actualizar(id_gasto, datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@gasto_blueprint.route('/gastos/<int:id_gasto>', methods=['DELETE'])
def eliminar_gasto(id_gasto):
    try:
        mensaje = gasto_service.eliminar(id_gasto)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200
