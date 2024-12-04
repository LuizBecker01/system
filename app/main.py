from flask import Blueprint, render_template, jsonify, request
from . import db
from datetime import datetime
import json
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

main = Blueprint('main', __name__)

# Modelo Status
class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

# Função para ler os sensores
def ler_sensor(id_sensor):
    return id_sensor % 2 == 0  # Alterna entre conectado/desconectado

# Função para atualizar o status
def atualizar_status():
    try:
        status_atualizado = Status.query.all()
        for sensor in status_atualizado:
            sensor.status = ler_sensor(sensor.id)  # Função que consulta o sensor
            sensor.timestamp = datetime.now()
        db.session.commit()
        print("Status atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar status: {str(e)}")


# Inicializando o agendador
scheduler = BackgroundScheduler()
scheduler.add_job(func=atualizar_status, trigger="interval", minutes=5)
scheduler.start()

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
        caminho_arquivo = os.path.join(os.getcwd(), 'app', 'status.json')
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:  # Certifique-se de usar 'utf-8'
            dados = json.load(arquivo)
        
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
