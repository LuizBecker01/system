from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializa o SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações de banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:luiz@localhost:5432/system'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o SQLAlchemy com o app
    db.init_app(app)

    # Importa e registra o blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
