from app.connection import engine,Base
from app import models

#Cria as ta belas do banco
Base.metadata.create_all(bind=engine)