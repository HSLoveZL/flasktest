# -*- coding=utf-8 -*-
from flask.ext.wtf import Form
from ..models import Category, User
from wtforms import ValidationError
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import Required, length, Regexp, EqualTo, Email
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class LoginForm(Form):
    username = StringField('Username', validators=[Required(), length(6, 64)])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField(u'登录')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), length(1, 64),
    					     Email()])
    username = StringField('Username', validators=[
    	Required(), length(6, 18), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
    					  'Username must have only letters,'
    				          'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
    	Required(), EqualTo('password2', message='Password must match')])
    password2 = PasswordField('Confirm_Password', validators=[Required()])
    #real_name = StringField('Real_Name', validators=[Required()])
    #registerkey = StringField('Register Code', validators=[Required()])
    submit = SubmitField('Register')
    
    def validate_email(self, field):
    	if User.query.filter_by(email=field.data).first():
    	    raise ValidationError('Email already registered')
    	    
    def validate_username(self, field):
    	if User.query.filter_by(username=field.data).first():
    	    raise ValidationError('Username already in use.')


class PostArticleForm(Form):
    title = StringField(u'标题', validators=[Required(), length(6, 64)])
    body = TextAreaField(u'内容')
    category_id = QuerySelectField(u'分类', query_factory=lambda: Category.query.all(
    ), get_pk=lambda a: str(a.id), get_label=lambda a: a.name)
    submit = SubmitField(u'发布')


class PostCategoryForm(Form):
    name = StringField(u'分类名', validators=[Required(), length(6, 64)])
    submit = SubmitField(u'发布')
