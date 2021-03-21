from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    story = db.relationship('Story', backref='story_author', lazy=True)
    chapter = db.relationship('Chapter', backref='chapter_author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f'<User: {self.username} | {self.email}>'

    def to_dict(self):
        return {
            'id':self.id,
            'username':self.username,
            'email':self.email,
            'password': self.password,
        }


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    story = db.relationship('Chapter', backref='story_chapter', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, user_id, chapter_title, content):
        self.title = title
        self.user_id = user_id

    def __repr__(self):
        return f'<Post: {self.title}>'

    def to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'date_created': self.date_created,
            'user_id': self.user_id,
            'username': self.story_author.username
        }


class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, content, user_id, story_id):
        self.title = title
        self.content = content
        self.story_id = story_id
        self.user_id = user_id

    def __repr__(self):
        return f'<Chapter: {self.title}>'

    def to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'content':self.content,
            'date_created': self.date_created,
            'story_id': self.story_chapter.id,
            'story_title': self.story_chapter.title,
            'user_id': self.chapter_author.id,
            'username': self.chapter_author.username,
            'date_created': self.date_created
        }
