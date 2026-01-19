from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='User Name')
    user_email = StringField(label='Email')
    pass1 = PasswordField(label='Password')
    pass2 = PasswordField(label='Confirm Password')
    submit_btn = SubmitField(label='Create Account')