from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, RadioField, SelectField

class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    age = IntegerField('Age')
    gender = RadioField('Gender', choices=[('m','Male'),('f','Female')])
    team = SelectField('Team', choices=[('red','Red'),('blue','Blue'),('green','Green')])
    submit = SubmitField('Sign Up')
