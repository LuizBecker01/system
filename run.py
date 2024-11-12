from app.connection import engine, Base
from app import models
from app import app

if __name__ == "__main__":
    with app.app_context():
        Base.metadata.create_all(bind=engine)   # Cria as tabelas do banco de dados
    app.run(host="0.0.0.0", port=8001, debug=True)