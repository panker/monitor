# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import config

SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost:3306/monitor?charset=utf8'
SQLALCHEMY_BINDS = {
    'xsg_stat':        'mysql://pirate:admin@192.168.1.135:3306/xsg_stat?charset=utf8',
    'xsg_ly':      'mysql://pirate:admin@192.168.1.135:3306/xsg_ly?charset=utf8'
}
db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
    #config[config_name].init_app(app)

    db = SQLAlchemy(app)

    CORS(app , resources=r'/*')

    #db.app = app

    # 注册蓝本
    # 增加auth蓝本


    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from app.main import app_main
    app.register_blueprint(app_main)


    # 附加路由和自定义的错误页面

    return app