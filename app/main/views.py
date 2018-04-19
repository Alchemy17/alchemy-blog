from . import main
from flask import Flask, render_template


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

@main.route('/add')
def add():
    return ''
