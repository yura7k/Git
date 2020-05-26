from wtforms import Form, StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class PostForm(Form):
    title = StringField('Title:', validators=[DataRequired()])
    body = TextAreaField('Body:', validators=[DataRequired()])
    submit = SubmitField('Create post')

class TagForm(Form):
    name = StringField('Name:', validators=[DataRequired()])
    submit = SubmitField('Create tag')

class UserForm(Form):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    phone = StringField('Phone number:', validators=[DataRequired()])
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password:', validators=[DataRequired(), EqualTo('password')])
    active = BooleanField('Is Active User: ')

    submit = SubmitField('Register')
