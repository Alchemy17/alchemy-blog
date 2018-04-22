from . import main
from flask import Flask, render_template, request, redirect, url_for
from ..models import Post, Comment, Reply
from datetime import datetime
from .. import db
from flask_login import login_required


@main.route('/')
def index():

    posts = Post.query.order_by(Post.date_posted.desc()). all()

    return render_template('index.html', posts = posts)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):

    post = Post.query.filter_by(id=post_id).one()
    return render_template('post.html', post = post)

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

@main.route('/comment', methods=['POST'])
def comment():

    comment = request.form['comment']
    comment = Comment(comment = comment, date_posted = datetime.now())

    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/reply', methods=['POST'])
def reply():


    reply = request.form['content']
    post = Post.query.all()
    
    reply = Reply(reply = reply, date_posted = datetime.now())
    
    db.session.add(reply)
    db.session.commit()
    return redirect(url_for('main.post', post_id = post.id))
    