# -*- coding=utf-8 -*-
from flask import current_app
from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask.ext.login import UserMixin


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    body = db.Column(db.Text)
    create_time = db.Column(db.DATETIME, default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

class Category(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='category')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    articles = db.relationship('Article', backref='user')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    confirmed = db.Column(db.Boolean, default=False)
    
    
    @property
    def password(self):
    	raise AttributeError(u'密码属性不正确')
    	
    @password.setter
    def password(self):
    	self.password_hash = generate_password_hash(password)
    	
    def verify_password(self, password):
    	return check_password_hash(self.password_hash, password)
    	
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})
        
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
    	
    	
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
