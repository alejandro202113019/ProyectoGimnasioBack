# controller/pago_controller.py
from flask import Blueprint, jsonify, request
from service.pago_service import PagoService

pago_blueprint = Blueprint('pago', __name__)
pago_service = PagoService()

@pago_blueprint.route('/pagos', methods=['GET'])
def obtener_pagos():
    try:
        pagos = pago_service.obtener_todos()
        return jsonify(pagos), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@pago_blueprint.route('/pagos/<int:id_pago>', methods=['GET'])
def obtener_pago(id_pago):
    try:
        pago = pago_service.obtener_por_id(id_pago)
        if pago:
            return jsonify(pago), 200
        return jsonify({'error': 'Pago no encontrado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@pago_blueprint.route('/pagos', methods=['POST'])
def crear_pago():
    try:
        datos = request.get_json()
        mensaje = pago_service.crear(datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@pago_blueprint.route('/pagos/<int:id_pago>', methods=['PUT'])
def actualizar_pago(id_pago):
    try:
        datos = request.get_json()
        mensaje = pago_service.actualizar(id_pago, datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@pago_blueprint.route('/pagos/<int:id_pago>', methods=['DELETE'])
def eliminar_pago(id_pago):
    try:
        mensaje = pago_service.eliminar(id_pago)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200
