# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(64), unique=True)
    role = db.Column(db.Integer, default=0x1)   # 普通用户0x1，admin用户0xf
    last_visit_ip = db.Column(db.String(20))
    last_visit_time = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def create_default_admin():
        user = User(username='admin', password=generate_password_hash('admin'), role=0xf)
        db.session.add(user)
        db.session.commit()


class RecordInfo(db.Model):
    __tablename__ = 'record_info'
    id = db.Column(db.Integer, primary_key=True)
    tool_for_vulnerability = db.Column(db.String(20), nullable=False)   # 发现漏洞的扫描工具：Nessus、NSFOCUS、WebInspect
    vulnerability_name = db.Column(db.Text, nullable=False)     # 漏洞名称
    vulnerability_level = db.Column(db.String(10), nullable=False)      # 漏洞等级：Critical、High、Medium、Low、None
    nessus_pluginID = db.Column(db.Integer, default=-1)     # 仅针对Nessus漏洞，需填发现漏洞对应的PluginID, 默认值为-1，表示没有PluginID
    vulnerable_link = db.Column(db.Text, nullable=True)     # 仅针对WebInspect漏洞，需要填写漏洞链接，默认为NULL
    detail_info = db.Column(db.Text, nullable=False)    # 漏洞备案链接或相关说明（CGSL操作系统问题的修复情况）
    record_project = db.Column(db.String(16), nullable=True)    # 漏洞所属项目

