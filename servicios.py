#servicios.py
from flask import Flask, request, jsonify
from Controllers.ClienteController import ClienteController

app = Flask(__name__)
cliente_controller = ClienteController()

@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    clientes = cliente_controller.obtener_todos_los_clientes()
    return jsonify(clientes), 200

@app.route('/clientes/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    cliente = cliente_controller.obtener_cliente_por_id(id_cliente)
    if cliente:
        return jsonify(cliente), 200
    return jsonify({"error": "Cliente no encontrado"}), 404

@app.route('/clientes', methods=['POST'])
def crear_cliente():
    datos = request.json
    resultado = cliente_controller.crear_cliente(datos)
    if resultado:
        return jsonify({"mensaje": "Cliente creado exitosamente"}), 201
    return jsonify({"error": "No se pudo crear el cliente"}), 400

@app.route('/clientes/<int:id_cliente>', methods=['PUT'])
def actualizar_cliente(id_cliente):
    datos = request.json
    resultado = cliente_controller.actualizar_cliente(id_cliente, datos)
    if resultado:
        return jsonify({"mensaje": "Cliente actualizado exitosamente"}), 200
    return jsonify({"error": "No se pudo actualizar el cliente"}), 400

@app.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    resultado = cliente_controller.eliminar_cliente(id_cliente)
    if resultado:
        return jsonify({"mensaje": "Cliente eliminado exitosamente"}), 200
    return jsonify({"error": "No se pudo eliminar el cliente"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
