import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
import pymysql


pymysql.install_as_MySQLdb()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    load_dotenv()
    # Configuracion de la conexion a la base de datos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + os.getenv('DATABASE_USER') + ':' + os.getenv(
        'DATABASE_PASSWORD') \
                                            + '@' + os.getenv('DATABASE_URL') + ':' + os.getenv('DATABASE_PORT') \
                                            + '/' + os.getenv('DATABASE_NAME')
    db.init_app(app)
    from main.resources.routes import routes
    app.register_blueprint(routes)
    return app

