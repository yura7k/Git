from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import re

from app import db

def slugify(title):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', title)

def db_commit(data):
    try:
        db.session.add(data)
        db.session.commit()
    except:
        print("Some wrong!!!")
        print(data)

post_tags = db.Table('post_tags',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))                                        
    )

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))
    
    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tad id: {}, name: {}>'.format(self.id, self.name)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(100), index=True, unique=True)
    phone = db.Column(db.String(15))
    username = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    user_type = db.Column(db.String(15))

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<ID {} - User {}>'.format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)