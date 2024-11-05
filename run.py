from app.connection import engine,Base
from app import models
from app import app

#Cria as ta belas do banco
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)