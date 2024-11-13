# controller/cliente_controller.py
from flask import Blueprint, jsonify, request
from service.cliente_service import ClienteService

cliente_blueprint = Blueprint('cliente', __name__)
cliente_service = ClienteService()

@cliente_blueprint.route('/clientes', methods=['GET'])
def obtener_clientes():
    try:
        clientes = cliente_service.obtener_todos_los_clientes()
        return jsonify(clientes), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@cliente_blueprint.route('/clientes/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    try:
        cliente = cliente_service.obtener_cliente_por_id(id_cliente)
        if cliente:
            return jsonify(cliente), 200
        return jsonify({'error': 'Cliente no encontrado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@cliente_blueprint.route('/clientes', methods=['POST'])
def crear_cliente():
    try:
        datos = request.get_json()
        mensaje = cliente_service.crear_cliente(datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@cliente_blueprint.route('/clientes/<int:id_cliente>', methods=['PUT'])
def actualizar_cliente(id_cliente):
    try:
        datos = request.get_json()
        mensaje = cliente_service.actualizar_cliente(id_cliente, datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@cliente_blueprint.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    try:
        mensaje = cliente_service.eliminar_cliente(id_cliente)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200