# -*- coding: utf-8 -*-

class BaseConfig:
    SECRET_KEY = "hard to guess string"
    SQLALCHEMY_DATABASE_URI = ""

class DevelopConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

config = {
    "dev": DevelopConfig,
    "pro": ProductionConfig
}