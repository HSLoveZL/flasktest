# -*- coding=utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from config import config
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.pagedown import PageDown


mail = Mail()
moment = Moment()
db = SQLAlchemy()
bootstrap = Bootstrap()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'admin.login'
login_manager.login_message = u'请登录之后再进行操作！'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    
    #if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        #from flask_sslify import SSLify
        #sslify = SSLify(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    
    return app
