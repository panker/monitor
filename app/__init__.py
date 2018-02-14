# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    CORS(app , resources=r'/*')

    db.init_app(app)
    db.app = app

    # 注册蓝本
    # 增加auth蓝本


    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from app.main import app_main
    app.register_blueprint(app_main)


    # 附加路由和自定义的错误页面

    return app