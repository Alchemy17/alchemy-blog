from . import db
from datetime import datetime

class Post(db.Model):

    __tablename__ = 'post'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)