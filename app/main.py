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
