from . import db
from datetime import datetime


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


#class Role(db.Model):
#    __tablename__ = 'roles'
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(64), unique=True)
    
#    def __repr__(self):
#    	return '<Role %r>' % self.name
    	
#    users = db.relationship('User', backref='role')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    real_name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='user')
    
    
#    def __repr__(self):
#    	return '<User %r>' % self.username
    	
#    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
