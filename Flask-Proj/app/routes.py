from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/Login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
