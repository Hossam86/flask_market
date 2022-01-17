from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    user_name = StringField('User Name')
    password_1 = PasswordField('Password')
    password_2 = PasswordField('Retype Password')
    submit = SubmitField('Submit')
