# app.py
from flask import Flask
from flask_cors import CORS

# Importamos los blueprints de los controladores
from controller.cliente_controller import cliente_blueprint
from controller.plan_controller import plan_blueprint
from controller.membresia_controller import membresia_blueprint
from controller.instructor_controller import instructor_blueprint
from controller.clase_controller import clase_blueprint
from controller.horario_controller import horario_blueprint
from controller.asistencia_controller import asistencia_blueprint
from controller.pago_controller import pago_blueprint
from controller.equipo_controller import equipo_blueprint
from controller.auth_controller import auth_blueprint

app = Flask(__name__)
CORS(app)

# Registramos los blueprints de cada controlador
app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
app.register_blueprint(cliente_blueprint, url_prefix='/api')
app.register_blueprint(plan_blueprint, url_prefix='/api')
app.register_blueprint(membresia_blueprint, url_prefix='/api')
app.register_blueprint(instructor_blueprint, url_prefix='/api')
app.register_blueprint(clase_blueprint, url_prefix='/api')
app.register_blueprint(horario_blueprint, url_prefix='/api')
app.register_blueprint(asistencia_blueprint, url_prefix='/api')
app.register_blueprint(pago_blueprint, url_prefix='/api')
app.register_blueprint(equipo_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
