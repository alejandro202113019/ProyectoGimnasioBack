# app.py
from flask import Flask
from flask_cors import CORS
from controller.cliente_controller import cliente_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(cliente_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)