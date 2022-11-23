from flask import Flask

from .main.routes import main
from .extensions import db

def create_app():
    app = Flask(__name__)

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zsjbpyuvqfuwfi:49cec541edabcecdd292aeef68fbc71875701b80ce40aec3dfbc1fa287a426da@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d226r984ts1duf'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(main)

    return app