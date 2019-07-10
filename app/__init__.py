# -*- coding: utf-8 -*-
from flask import Flask
from config import config
from models import db


def create_app(configname):
    # create Flask object
    app = Flask(__name__)
    app.secret_key = config[configname].SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = config[configname].SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config[configname].SQLALCHEMY_TRACK_MODIFICATIONS

    # plugin initial
    db.init_app(app)

    # register blueprint
    from .auth import auth as auth_blueprint
    from .index import index as index_blueprint
    from .api import api as api_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')
    app.register_blueprint(index_blueprint, url_prefix='/index')
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

