# -*- coding: utf-8 -*-
class BaseConfig:
    SECRET_KEY = "hard to guess string"
    SQLALCHEMY_DATABASE_URI = "mysql://user:password@ip:port/database?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


config = {
    "dev": DevelopConfig,
    "pro": ProductionConfig
}
