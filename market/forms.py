from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email

class RegisterForm(FlaskForm):
    username = StringField(label='User Name', validators=[Length(min=2,max=10), DataRequired()])
    email_address=StringField(label='Email Address', validators=[Email()])
    password1 = PasswordField(label='Password', validators=[Length(min=6)])
    password2 = PasswordField(label='Retype Password',validators=[EqualTo(password1, message="incorrrect password matching")])
    submit = SubmitField(label='Create Account')
