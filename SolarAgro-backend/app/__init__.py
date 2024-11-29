# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_jwt_extended import JWTManager


# db = SQLAlchemy()
# migrate = Migrate()
# jwt = JWTManager()

# def create_app(config_class='app.config.Config'):
#     """ Função para criar e configurar a aplicação Flask """
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     # Inicializando as extensões
#     db.init_app(app)
#     migrate.init_app(app, db)
#     jwt.init_app(app)

#     # Registrando as rotas
#     from App import routes
#     app.register_blueprint(routes.bp)

#     return app




# from flask import Flask
# from app.routes import api

# def create_app():
#     app = Flask(__name__, template_folder='templates', static_folder='static')

#     # Registrar o Blueprint
#     app.register_blueprint(api)

#     return app

















from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()  # Instância do SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Configurações a partir do arquivo config.py
    db.init_app(app)  # Inicializa a instância de db

    # Registrar os blueprints
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app

