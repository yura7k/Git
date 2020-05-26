from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemySessionUserDatastore, Security, current_user
# from flask_script import Manage

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# config DB and migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# config Flask-ADMIN
from app.models import *

# перевіряємо чи користувач ADMIN чи може івін переходити в адмінку
# перевизначаємо методи is_accessible та inaccessible_callback клас AdminIndexView
# варіант 1
# class AdminView(ModelView):
#     def is_accessible(self):
#         return current_user.has_role('ADMIN')
    
#     def inaccessible_callback(self, **kwargs):
#         return redirect(url_for('security.login', next=request.url))

class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('ADMIN')
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))

# перевизначаємо метод on_model_change клас ModelView, щоб автоматично генерувались поcилання
class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)

admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView())
admin.add_view(BaseModelView(Post, db.session))
admin.add_view(BaseModelView(Tag, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))

# comfig Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)

from app import view, models

# не вийшло з імпортом blueprint
# from posts.blueprint import posts 

# app.register_blueprint(posts, url_prefix='/blog')
