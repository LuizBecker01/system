from flask import Blueprint, render_template, jsonify, request
from . import db
from datetime import datetime
import json
import os

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
def mhcolleb():
    return render_template('mhCOLLAB.html')

# Rota psCOLLAB
@main.route('/psCOLLAB')
def pscolleb():
    return render_template('psCOLLAB.html')

# Rota OEE
@main.route('/OEE')
def oee():
    return render_template('OEE.html')

# Rota mhMonitoramento
@main.route('/mhMonitoramento')
def mhmonitoramento():
    try:
        # Carregar dados do arquivo JSON
        caminho_arquivo = os.path.join(os.getcwd(), 'app', 'status.json')
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        
        # Passar os dados para o template
        return render_template('mhMonitoramento.html', dados=dados)
    
    except Exception as e:
        return jsonify({"erro": f"Erro ao carregar os dados: {str(e)}"})

# Rota psMonitoramento
@main.route('/psMonitoramento')
def psmonitoramento():
    return render_template('psMonitoramento.html')

# Rota OEEMonitoramento
@main.route('/OEEMonitoramento')    
def oeeMonitoramento():
    return render_template('OEEMonitoramento.html')
