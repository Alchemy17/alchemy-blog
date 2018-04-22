from . import db, admin, login_manager
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Post(db.Model):

    __tablename__ = 'post'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)
    comment_id = db.Column(db.Integer,db.ForeignKey('comment.id'))

class Comment(db.Model):

    __tablename__ = 'comment'
    
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    comment = db.Column(db.Text)
    comments = db.relationship('Post',backref = 'comment',lazy="dynamic")
    reply_id = db.Column(db.Integer,db.ForeignKey('reply.id'))


class Reply(db.Model):

    __tablename__ = 'reply'
    
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    reply = db.Column(db.Text)
    comments = db.relationship('Comment',backref = 'reply',lazy="dynamic")

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
    

class MyModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.is_admin:
            return True
        else:
            return False

admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Post, db.session))
admin.add_view(MyModelView(Comment, db.session))
admin.add_view(MyModelView(Reply, db.session))