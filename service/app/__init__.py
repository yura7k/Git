from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
# from flask_script import Manage

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# config DB adn migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# config ADMIN
from app.models import *
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))
admin.add_view(ModelView(User, db.session))

from app import view, models

# не вийшло з імпортом blueprint
# from posts.blueprint import posts 

# app.register_blueprint(posts, url_prefix='/blog')