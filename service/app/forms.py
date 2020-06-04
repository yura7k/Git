from wtforms import *
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo

from flask_security.forms import RegisterForm
from flask_security import current_user

from app import security
from app.models import Service

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
    # myChoices = [1,2,3,4,5]
    # myField = SelectField(u'Field name', choices = myChoices, validators = [DataRequired()])

    def __init__(self, current_user, service_list):
        Form.__init__(self)
        self.current_user = current_user
        self.service_list = []

        # for item in service_list:
        #     self.service_list.append(item.name)

        if not current_user.is_authenticated:
            setattr(OrderForm, 'name', StringField('ПІБ:', validators=[DataRequired()]))
            setattr(OrderForm, 'email', StringField('E-mail:', validators=[DataRequired(), Email()]))
            setattr(OrderForm, 'phone', StringField('Номер телефону:', validators=[DataRequired()]))

        setattr(OrderForm, 'service', SelectField(u'Вид ремонту:', 
                                                choices=[(item.id, item.name)
                                                        for item in service_list], 
                                                validators=[DataRequired()]))
        setattr(OrderForm, 'name_auto', StringField('Модель авто:', validators=[DataRequired()]))
        setattr(OrderForm, 'vin', StringField('VIN:', validators=[DataRequired()]))
        setattr(OrderForm, 'timefrom', DateField('Дата звернення:', validators=[DataRequired()]))
        setattr(OrderForm, 'comment', StringField('Коментар:', validators=[DataRequired()]))

        setattr(OrderForm, 'submit', SubmitField('Відправити'))  

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')