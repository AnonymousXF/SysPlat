# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(64), nullable=True, unique=True)
    role = db.Column(db.Integer, default=0x1)   # 普通用户0x1，admin用户0xf
    last_visit_ip = db.Column(db.String(20))
    last_visit_time = db.Column(db.DateTime, default=datetime.utcnow)

'''
机柜  槽位  机型  环境  组件规划  操作系统  大网  小网  IPMI地址  IPMI调试  IPMI调试  负责人  项目  资产编号
'''    
