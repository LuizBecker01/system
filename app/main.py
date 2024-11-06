# app/main.py
from flask import Blueprint, render_template, jsonify, request
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

# Modelo Status
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

# Rota mhCOLLAB
@main.route('/mhCOLLAB')
def mh_collab():
    return render_template('mhCOLLAB.html')

# Rota para adicionar um novo status
@main.route('/add_status', methods=['POST'])
def add_status():
    name = request.form.get('name')
    status_value = request.form.get('status').lower() in ['true', '1', 'yes']
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
