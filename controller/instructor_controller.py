# controller/instructor_controller.py
from flask import Blueprint, jsonify, request
from service.instructor_service import InstructorService

instructor_blueprint = Blueprint('instructor', __name__)
instructor_service = InstructorService()

@instructor_blueprint.route('/instructores', methods=['GET'])
def obtener_instructores():
    try:
        instructores = instructor_service.obtener_todos()
        return jsonify(instructores), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@instructor_blueprint.route('/instructores/<int:id_instructor>', methods=['GET'])
def obtener_instructor(id_instructor):
    try:
        instructor = instructor_service.obtener_por_id(id_instructor)
        if instructor:
            return jsonify(instructor), 200
        return jsonify({'error': 'Instructor no encontrado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@instructor_blueprint.route('/instructores', methods=['POST'])
def crear_instructor():
    try:
        datos = request.get_json()
        mensaje = instructor_service.crear(datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@instructor_blueprint.route('/instructores/<int:id_instructor>', methods=['PUT'])
def actualizar_instructor(id_instructor):
    try:
        datos = request.get_json()
        mensaje = instructor_service.actualizar(id_instructor, datos)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200

@instructor_blueprint.route('/instructores/<int:id_instructor>', methods=['DELETE'])
def eliminar_instructor(id_instructor):
    try:
        mensaje = instructor_service.eliminar(id_instructor)
        return jsonify({'message': mensaje}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 200
