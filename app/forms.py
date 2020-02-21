from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class EditProfileForm(FlaskForm):
    """ form for user profile updates
    
    Parameters
    ----------
    FlaskForm : flask form
        form auto generated by flask
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=17)])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError("Username has already been taken!")


class RegistrationForm(FlaskForm):
    """Registration
    
    Parameters
    ----------
    FlaskForm : Form
        User registration form
    
    Raises
    ------
    ValidationError
        Username is required
    ValidationError
        Passwords must match
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username has already been taken!")
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is  not None:
            raise ValidationError("Email already in use!")



class LoginForm(FlaskForm):
    username = StringField("Username", validators=[(DataRequired())])
    password = PasswordField("Passsword", validators=[(DataRequired())])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign In")
    


