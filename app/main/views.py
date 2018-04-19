from . import main
from flask import Flask, render_template, request, redirect, url_for
from ..models import Post
from datetime import datetime
from .. import db


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/post')
def post():
    return render_template('post.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/new')
def new():
    return render_template('new_post.html')

@main.route('/add', methods=['POST'])
def add():

    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']
    
    post = Post(title = title, subtitle = subtitle, author = author, content = content, date_posted = datetime.now())
    
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('main.index'))
    