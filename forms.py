from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from datetime import datetime

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    title = StringField('Task Title', validators=[DataRequired()])
    description = StringField('Description')
    date_due = DateTimeField('Due Date', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Save Task')

    def validate_date_due(self, date_due):
        if date_due.data < datetime.today().date():
            raise ValidationError('Due date must be in the future')