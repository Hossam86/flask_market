from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    user_name = StringField(label='User Name')
    email_address=StringField(label='Email Address')
    password_1 = PasswordField(label='Password')
    password_2 = PasswordField(label='Retype Password')
    submit = SubmitField(label='Create Account')
