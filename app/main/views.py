# -*- coding=utf-8 -*-
from . import main
from flask import render_template, redirect, url_for, flash, request
from ..models import Article


@main.route('/')
def index():
    a = Article.query.all()
    return render_template('index.html', list=a)
    
    
@main.route('/read/', methods=['GET'])
def read():
    a = Article.query.filter_by(id=request.args.get('id')).first()
    if a is not None:
        return render_template('read.html', a=a)
    flash(u'未找到相关文章')
    return redirect(url_for('main.index'))
