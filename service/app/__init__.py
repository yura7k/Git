from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from app import view

db = SQLAlchemy(app)

# не вийшло з імпортом blueprint
# from posts.blueprint import posts 

# app.register_blueprint(posts, url_prefix='/blog')