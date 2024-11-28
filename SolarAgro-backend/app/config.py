# import os

# class Config:
#     """ Configurações gerais do Flask """
#     SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey') 
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

   
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///solaragro.db')

    
#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwtsecretkey')  
#     JWT_ACCESS_TOKEN_EXPIRES = 3600  

    
#     TEMPLATES_AUTO_RELOAD = True
#     STATIC_FOLDER = 'static'
#     TEMPLATES_FOLDER = 'templates'

    
#     MAIL_SERVER = 'smtp.mailtrap.io'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.getenv('MAIL_USERNAME')
#     MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')




# import os

# class Config:
#     SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///solaragro.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False










import os

class Config:
    # Defina a URI do banco de dados aqui
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')  # Fallback para SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desabilita a notificação de modificações
