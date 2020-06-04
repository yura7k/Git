from datetime import datetime
import re
import jwt
from time import time
from app import db, app

from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import UserMixin, RoleMixin, utils

# конвертує назву в URL подібний текст
def slugify(title):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', title)

# запис даних форми до БД
def db_commit(data):
    try:
        db.session.add(data)
        db.session.flush()  
        db.session.commit()
        # print(data.id) for testing
        return data.id
    except:
        print("Some wrong!!!")
        print(data)

# проміжна таблиця для звязбу багато-до-багатьох Post-to-Tag
post_tags = db.Table('post_tags',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))                                   
    )

# Таблиця статей сайту
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tags = db.relationship('Tag', secondary=post_tags, backref='posts', lazy='dynamic')
    
    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)

# Таблиця тагів, які можуть містити статті
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tad ID: {}, name: {}>'.format(self.id, self.name)

# проміжна таблиця для звязбу багато-до-багатьох User-to-Roles
roles_users = db.Table('roles_users',
                    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
    )
# Таблиця користувачів, успадковуємо методи від flask-security UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(100), index=True, unique=True)
    phone = db.Column(db.String(15))
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))
    registered = db.Column(db.DateTime(), default=datetime.now())
    active = db.Column(db.Boolean())
    
    roles = db.relationship('Role', secondary=roles_users, backref='users', lazy='dynamic')
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    orders = db.relationship('Order', backref='orders', lazy='dynamic')

    def __repr__(self):
        return '<ID: {}; User: {} Active: {}>'.format(self.id, self.username, self.active)

    def set_password(self, password):
        self.password = utils.encrypt_password(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


# таблиця ролей успадковуємо методи від flask-security RoleMixin
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
    
    def __repr__(self):
        return 'Role: {}'.format(self.name)

# проміжна таблиця для звязбу багато-до-багатьох Order-to-Service
order_service = db.Table('order_service',
                    db.Column('order_id', db.Integer(), db.ForeignKey('order.id')),
                    db.Column('service_id', db.Integer(), db.ForeignKey('service.id'))
    )

# таблиця запису клієнтів
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name_auto = db.Column(db.String(150))
    vin = db.Column(db.String(50))
    timefrom = db.Column(db.DateTime(), default=datetime.now())
    timeto = db.Column(db.DateTime(), default=datetime.now())
    comment = db.Column(db.Text)

    services = db.relationship('Service', secondary=order_service, backref='orders', lazy='dynamic')

    def __repr__(self):
        return '<ID: {}; User: {} VIN: {}>'.format(self.id, self.user_id, self.vin)

# таблиця типу робіт сервісу
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    description = db.Column(db.Text)
    deadline = db.Column(db.Integer)
    price = db.Column(db.Float)
    created = db.Column(db.DateTime(), default=datetime.now())

    category_id = db.Column(db.Integer, db.ForeignKey('service_category.id'))
    
    def __repr__(self):
        return '<ID: {}; Name: {}>'.format(self.id, self.name)

# таблиця категорії робіт
class Service_category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    category = db.Column(db.String(150))
    description = db.Column(db.String(255))

    categorys = db.relationship('Service', backref='category', lazy='dynamic')
    
    def __repr__(self):
        return 'Category: {}'.format(self.category)
    