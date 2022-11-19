from bughunter import app, images
from flask import render_template, redirect, url_for, flash, request
# from werkzeug.utils import secure_filename
from bughunter.models import User, Project, Domain
from bughunter.forms import RegisterForm, LoginForm, ProjectForm, DomainForm
from bughunter import db
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date
import os

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/projects', methods=['GET', 'POST'])
@login_required
def projects_page():
    form = ProjectForm()
    if request.method == "POST":
        if form.is_submitted():
            filename= images.save(form.image.data)
            d1 = date.today().strftime("%d/%m/%Y")
            project_to_create = Project(name=form.name.data,
                                image=filename,
                                creation_date=d1,
                                description=form.description.data,
                                owner=current_user.id)
            db.session.add(project_to_create)
            db.session.commit()
            flash(f"Projeto criado com sucesso!", category='success')
            return redirect(url_for('projects_page'))
        if form.errors != {}: #If there are not errors from the validations
            for err_msg in form.errors.values():
                flash(f'Ocorreu um erro ao criar o projeto: {err_msg}', category='danger')

            return redirect(url_for('projects_page'))

    if request.method == "GET":
        projects = Project.query.filter_by(owner=current_user.id)
        return render_template('projects.html', form=form, projects=projects)

@app.route('/projects/<project>', methods=['GET', 'POST'])
@login_required
def directories_page(project):
    form = DomainForm()
    if request.method == "POST":
        if form.is_submitted():
            for directory in form.directory.data.splitlines():
                domain_to_create = Domain(name=directory,
                                project=Project.query.filter_by(name=project).first().id)
                db.session.add(domain_to_create)
            db.session.commit()
            
        
        if form.errors != {}: #If there are not errors from the validations
            for err_msg in form.errors.values():
                flash(f'Ocorreu um erro ao adicionar diretórios ao projeto: {err_msg}', category='danger')

        return redirect(url_for('directories_page', project=project))
    if request.method == "GET":
        domains = Domain.query.filter_by(project=Project.query.filter_by(name=project).first().id)
        return render_template('domains.html', form=form, domains=domains)

@app.route('/deleteproject/<project>')
@login_required
def delete_project_page(project):
    imagename = Project.query.filter_by(name=project).first().image
    os.remove(f'bughunter/static/{imagename}')
    #remove os domínios do site
    Domain.query.filter_by(project=Project.query.filter_by(name=project).first().id).delete()

    Project.query.filter_by(name=project).delete()
    db.session.commit()
    flash(f"Você deletou com sucesso o projeto {project}", category='info')
    return redirect(url_for("projects_page"))

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Conta criada com sucesso! Você está logado como {user_to_create.username}", category='success')
        return redirect(url_for('projects_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'Ocorreu um erro ao criar o usuário: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Successo! Agora você está logado como: {attempted_user.username}', category='success')
            return redirect(url_for('projects_page'))
        else:
            flash('Nome de usuário ou senha não são compatíveis! Tente novamente', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("Você foi deslogado!", category='info')
    return redirect(url_for("home_page"))
