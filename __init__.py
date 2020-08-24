from flask import Flask
from flask_login import LoginManager
from .database.db import GerenciarBanco
from .models.usuario import Usuario

gerenciar_banco = GerenciarBanco()
conn = gerenciar_banco.conectar()
cursor = conn.cursor()

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'ThisismysecretKey'

    
    login_manager.init_app(app)


    from .auth import auth
    app.register_blueprint(auth)

    from .main import main
    app.register_blueprint(main)

    return app


