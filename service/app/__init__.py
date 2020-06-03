from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_mail import Mail, Message

from flask_security import SQLAlchemySessionUserDatastore, Security, current_user
# from flask_script import Manage

from flask_googlemaps import GoogleMaps

from config import Config

app = Flask(__name__, static_url_path='')
app.config.from_object(Config)

# config DB and migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# config Flask Mail
mail = Mail(app)

# config Flask-ADMIN
from app.models import *

# перевіряємо чи користувач ADMIN чи може івін переходити в адмінку
# перевизначаємо методи is_accessible та inaccessible_callback клас AdminIndexView
class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('ADMIN')
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))

# перевизначаємо метод on_model_change Admin панелі
# клас ModelView, щоб автоматично генерувались поcилання
class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)

# клас ModelView Admin панелі, щоб поля password не відображались в адмінці
class UserModelView(ModelView):
    # Не показувати пароль у списку Users
    column_exclude_list = list = ('password',)

    # Не включайте стандартне поле пароля під час створення або редагування User
    form_excluded_columns = ('password',)
    
admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView())
admin.add_view(BaseModelView(Post, db.session))
admin.add_view(BaseModelView(Tag, db.session))
admin.add_view(UserModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Service, db.session))
admin.add_view(ModelView(Service_category, db.session))
admin.add_view(ModelView(Order, db.session))

# comfig Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)

# comfig Flask-Google maps
maps = GoogleMaps(app)

from app import view, models

# не вийшло з імпортом blueprint
# from posts.blueprint import posts 

# app.register_blueprint(posts, url_prefix='/blog')
