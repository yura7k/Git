from wtforms import Form, StringField, TextAreaField, SubmitField, PasswordField, BooleanField, DateField
from wtforms.validators import DataRequired, Email, EqualTo

from flask_security.forms import RegisterForm

class NewsForm(Form):
    title = StringField('Заголовок:', validators=[DataRequired()])
    body = TextAreaField('Текст новини:', validators=[DataRequired()])
    submit = SubmitField('Створити новину')

class TagForm(Form):
    name = StringField('Назва:', validators=[DataRequired()])
    submit = SubmitField('Створити tag')

class RegistrationForm(RegisterForm):
    name = StringField('ПІБ:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    phone = StringField('Номер телефону:', validators=[DataRequired()])
    username = StringField('Ім’я користувача:', validators=[DataRequired()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    password_confirm = PasswordField('Повтор паролю:', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Зареєструвати')

class OrderForm(Form):
    service = StringField('Вид ремонту:', validators=[DataRequired()])
    name_auto = StringField('Модель авто:', validators=[DataRequired()])
    vin = StringField('VIN:', validators=[DataRequired()])
    timefrom = DateField('Дата звернення:', validators=[DataRequired()])
    comment = StringField('Коментар:', validators=[DataRequired()])

    submit = SubmitField('Відправити')
