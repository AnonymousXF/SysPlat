# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(configname):
    # create Flask object
    app = Flask(__name__)
    app.secret_key = config[configname].SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = config[configname].SQLALCHEMY_DATABASE_URI

    # plugin initial
    db.init_app(app)

    return app

