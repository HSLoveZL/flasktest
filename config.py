# -*- coding=utf-8-*-
import os
from logging.handlers import RotatingFileHandler
import logging


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    HONGSH_MAIL_SUBJECT_PREFIX = '[HongSh]'
    HONGSH_MAIL_SENDER = 'HongSh Admin hongsh.zl@foxmail.com'
    HONGSH_ADMIN = os.environ.get('HONGSH_ADMIN')
    HONGSH_POSTS_PER_PAGE = 20
    HONGSH_FOLLOWERS_PER_PAGE = 50
    HONGSH_COMMENTS_PER_PAGE = 30
    HONGSH_SLOW_DB_QUERY_TIME=0.5
    
    @staticmethod
    def init_app(app):
        pass
    	
    	
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:hs123@127.0.0.1/flasktest'


config = {
    'default':DevelopmentConfig
}
