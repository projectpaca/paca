from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Användarnamn', validators=[DataRequired()])
    password = PasswordField('Lösenord', validators=[DataRequired()])
    remember_me = BooleanField('Kom ihåg mig')
    submit = SubmitField('Logga in')


class RegistrationForm(FlaskForm):
    username = StringField('Användarnamn', validators=[DataRequired()])
    email = StringField('Epost', validators=[DataRequired(), Email()])
    password = PasswordField('Lösenord', validators=[DataRequired()])
    password2 = PasswordField(
        'Upprepa lösenord', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrera dig')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Vad god välj ett annat användarnamn.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Var god välj en annan epostadress.')


class EditProfileForm(FlaskForm):
    username = StringField('Användarnamn', validators=[DataRequired()])
    about_me = TextAreaField('Om mig', validators=[Length(min=0, max=140)])
    submit = SubmitField('Skicka')
    
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Var god välj ett annat användarnamn.')


class PostForm(FlaskForm):
    post = TextAreaField('När kan du jobba?', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Skicka')