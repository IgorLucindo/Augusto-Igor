from bughunter import app
from flask import render_template, redirect, url_for, flash, request
# from market.models import Item, User
# from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
# from market import db
# from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')