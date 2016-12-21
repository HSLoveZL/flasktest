# -*- coding=utf-8-*-


class Config:
    SECRET_KEY = 'Hs1123pYthDf'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    
    @staticmethod
    def init_app(app):
    	_handler = RotatingFileHandler(
    	    'app.log', maxBytes=10000, backupCount=1)
    	_handler.setLevel(logging.WARNING)
    	app.logger.addHandler(_hangler)
    	
    	
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://flask:flask@127.0.0.1/flask_dev'


config = {
    'default':DevelopmentConfig
}
