from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manage

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import view, models


# не вийшло з імпортом blueprint
# from posts.blueprint import posts 

# app.register_blueprint(posts, url_prefix='/blog')