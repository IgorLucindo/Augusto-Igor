from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from bughunter.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    image = FileField(validators=[FileRequired()])
    submit = SubmitField(label='Sign In')


class ProjectForm(FlaskForm):
    # name = db.Column(db.String(length=30), nullable=False, unique=True)
    # image = db.Column(db.String(length=1024)) # url da imagem
    # date_of_start = db.Column(db.String(length=10), nullable=False)
    # date_of_end = db.Column(db.String(length=10))
    # description = db.Column(db.String(length=1024), nullable=False, unique=True)
    # owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    # domain = db.relationship('Domain', backref='project_originated', lazy=True)

    name = StringField(label='Nome do projeto: ', validators=[DataRequired()])
    image = StringField(label='URL da imagem do projeto: ', validators=[DataRequired()])
    description = StringField(label='Descrição do projeto: ', validators=[DataRequired()])
    submit = SubmitField(label='Adicionar')