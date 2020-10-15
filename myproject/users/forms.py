from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError
from myproject import models

SECRET_KEY = 'c308e5fb-b27d-44c9-b9e4-f07f5516609f'


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    key = StringField('Credential key', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_user(self, field):
        if models.User.query.filter_by(username=field.data).first():
            raise ValidationError("Username has been already used!")

    def check_key(self, field):
        if field.key.data != SECRET_KEY:
            raise ValidationError("wrong sescret key!")


class AuthIPForm(FlaskForm):
    choice = RadioField('Pick method:', choices=[('auth','Authentication'),('deauth','Remove Authentication')])
    ip = StringField('IP')
    submit = SubmitField('Submit')

