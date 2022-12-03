from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from bughunter.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Nome de usuário já existe! Tente um nome diferente')
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Endereço de email já existe! Por favor, tente um endereço diferente')

    username = StringField(label='Nome de usuário:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Senha:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirmar Senha:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Criar Conta')

class LoginForm(FlaskForm):
    username = StringField(label='Nome de usuário:', validators=[DataRequired()])
    password = PasswordField(label='Senha:', validators=[DataRequired()])
    image = FileField(validators=[FileRequired()])
    submit = SubmitField(label='Sign In')


class ProjectForm(FlaskForm):
    name = StringField(label='Nome do projeto: ', validators=[DataRequired()])
    description = TextAreaField(label='Descrição do projeto: ', validators=[DataRequired()])
    image = FileField(validators=[FileRequired()])
    submit = SubmitField(label='Adicionar')

class DomainForm(FlaskForm):
    directory= TextAreaField(label='Insira novos domínios a serem analisados: ', validators=[DataRequired()])
    submit = SubmitField(label='Adicionar')

class DelDomainForm(FlaskForm):
    submit = SubmitField(label='Remover')

class EditDomainForm(FlaskForm):
    description = TextAreaField(label='Descrição: ')
    services = SelectField(label='Sobre serviços rodando na máquina: ',choices=[(3, 'Desconhecido'),(1, 'Web'),(2,'Não Web'),(4,'Não Responde')])
    status = SelectField(label='Status da análise: ',choices=[(2,'Não analisado'), (1,'Em análise'),(3,'Analisado'),(4,'Análise Adiada')])
    submit = SubmitField(label='Editar')