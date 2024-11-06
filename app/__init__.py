from flask import Flask
from app.connection import engine
from app.models import Base 

# Criação do objeto Flask
app = Flask(__name__)

# Configurações de banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:2404@localhost:5432/system"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Associando o objeto 'app' aos modelos e engine
Base.metadata.bind = engine
