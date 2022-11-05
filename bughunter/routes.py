from bughunter import app
from flask import render_template, redirect, url_for, flash, request
from bughunter.models import User
from bughunter.forms import RegisterForm, LoginForm, ProjectForm
from bughunter import db
from flask_login import login_user, logout_user, login_required, current_user

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
    # if request.method == "POST":
    #     #Purchase Item Logic
    #     purchased_item = request.form.get('purchased_item')
    #     p_item_object = Item.query.filter_by(name=purchased_item).first()
    #     if p_item_object:
    #         if current_user.can_purchase(p_item_object):
    #             p_item_object.buy(current_user)
    #             flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
    #         else:
    #             flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!", category='danger')

    #     return redirect(url_for('projects_page'))

    if request.method == "GET":
        form = ProjectForm()
        return render_template('projects.html', form=form)


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
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('projects_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

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
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('projects_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))
