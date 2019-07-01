# -*- coding: utf-8 -*-
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True, unique=True)
    role = db.Column(db.Integer, default=0x1)   # 普通用户0x1，admin用户0xf
    last_visit_ip = db.Column(db.String)
    last_visit_time = db.Column(db.DateTime, default=datetime.utcnow)
