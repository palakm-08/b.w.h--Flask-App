from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='User Name', validators=[Length(min=4, max=16), DataRequired()])
    user_email = StringField(label='Email', validators=[Email(), DataRequired()])
    pass1 = PasswordField(label='Password', validators=[Length(min=8, max=15), DataRequired()])
    pass2 = PasswordField(label='Confirm Password', validators=[EqualTo('pass1'), DataRequired()])
    submit_btn = SubmitField(label='Create Account')