from flask import Flask, jsonify, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Configurações do app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2404@localhost:5432/system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o SQLAlchemy
db = SQLAlchemy(app)

# Blueprint setup
main = Blueprint('main', __name__)

class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

# Rota principal
@main.route('/')
def index():
    return render_template('index.html')

# Rota para adicionar um novo status
@main.route('/add_status', methods=['POST'])
def add_status():
    name = request.form.get('name')
    status_value = request.form.get('status').lower() in ['true', '1', 'yes']  # Verifica se o valor do campo 'status' é 'true'
    novo_status = Status(name=name, status=status_value)
    db.session.add(novo_status)
    db.session.commit()
    return jsonify({'message': 'Status adicionado com sucesso!'})

# Rota para consultar os registros de status
@main.route('/status', methods=['GET'])
def get_status():
    status_list = Status.query.all()
    return jsonify([{'id': s.id, 'name': s.name, 'status': s.status, 'timestamp': s.timestamp} for s in status_list])

# Rota para atualizar o status de uma máquina pelo id
@main.route('/update_status/<int:id>', methods=['PUT'])
def update_status(id):
    status_entry = Status.query.get(id)
    if not status_entry:
        return jsonify({'message': 'Status não encontrado!'}), 404

    status_entry.status = request.form.get('status') == 'true'
    db.session.commit()
    return jsonify({'message': 'Status atualizado com sucesso!'})

# Registrando o blueprint
app.register_blueprint(main)

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()
