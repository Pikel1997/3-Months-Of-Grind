from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Pikel Juice',
        'title': 'Post 1',
        'content': 'First post ever!!',
        'date_posted': 'April 13, 2022',
    },
    {
        'author': 'Jikel Puice',
        'title': 'Post 2',
        'content': 'Second post ever!!',
        'date_posted': 'April 14, 2022',
    },
]


@app.route("/")
@app.route("/Home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/About")
def about():
    return render_template('about.html', title="About Us")


@app.route("/Register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created, you are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/Login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/Logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/Account")
@login_required
def account():
    return render_template('account.html', title='Account')