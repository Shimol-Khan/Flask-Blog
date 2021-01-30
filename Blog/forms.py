from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[
                DataRequired(),
                Length(min=6, max=32)
            ])

    contact_number = StringField('Contact Number', validators=[
                DataRequired(),
                Length(min=11)
            ])

    address = StringField('Address', validators=[
                DataRequired(),
                Length(min=16)
            ])
    
    email = StringField('Email', validators=[
                DataRequired(), email()
            ])
    
    password = PasswordField('Password', validators=[
                DataRequired()
                ])

    confirm_password = PasswordField('Confirm Password', validators=[
                DataRequired(),
                EqualTo('password')
    ])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                DataRequired(), email()
            ])
    
    password = PasswordField('Password', validators=[
                DataRequired()
                ])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')
