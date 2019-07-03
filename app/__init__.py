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
    from .login import login as login_blueprint
    app.register_blueprint(login_blueprint, url_prefix='/')

    return app

