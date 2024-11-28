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
from flask_login import LoginManager
from .config import Config

# Inicializa as extensões
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_filename='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)  # Carregando as configurações

    print(app.config['SQLALCHEMY_DATABASE_URI'])  # Verificando a URI do banco de dados

    # Inicializa o banco de dados e o login manager
    db.init_app(app)
    login_manager.init_app(app)

    # Função user_loader
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User  # Importação para evitar circular import
        return User.query.get(int(user_id))

    # Registra as rotas
    from . import routes
    app.register_blueprint(routes.bp)

    return app

