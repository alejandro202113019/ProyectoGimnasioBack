# controller/plan_controller.py
from flask import Blueprint, jsonify, request
from service.plan_service import PlanService

plan_blueprint = Blueprint('plan', __name__)
plan_service = PlanService()

@plan_blueprint.route('/planes', methods=['GET'])
def obtener_planes():
    try:
        planes = plan_service.obtener_todos()
        return jsonify(planes), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@plan_blueprint.route('/planes/<int:id_plan>', methods=['GET'])
def obtener_plan(id_plan):
    try:
        plan = plan_service.obtener_por_id(id_plan)
        if plan:
            return jsonify(plan), 200
        return jsonify({'error': 'Plan no encontrado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@plan_blueprint.route('/planes', methods=['POST'])
def crear_plan():
    try:
        datos = request.get_json()
        mensaje = plan_service.crear(datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@plan_blueprint.route('/planes/<int:id_plan>', methods=['PUT'])
def actualizar_plan(id_plan):
    try:
        datos = request.get_json()
        mensaje = plan_service.actualizar(id_plan, datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@plan_blueprint.route('/planes/<int:id_plan>', methods=['DELETE'])
def eliminar_plan(id_plan):
    try:
        mensaje = plan_service.eliminar(id_plan)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200
