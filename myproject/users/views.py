from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from myproject import db
from myproject.models import User
from myproject.users.forms import *
from myproject.users.updateIP import *


users = Blueprint('users', __name__)



@users.route('/')
def index():
    form = LoginForm()
    return render_template('login.html',form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in Successfully!')
            return redirect(url_for('users.authenticateip'))
    return render_template('login.html',form=form)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.key.data != SECRET_KEY:
            flash("wrong sescret key!")
            return render_template('register.html', form=form)

        user = User(form.username.data, form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users.route('/authenticate', methods=['GET', 'POST'])
@login_required
def authenticateip():
    form = AuthIPForm()
    if form.validate_on_submit():
        link = "https://blazingseollc.com/proxy/dashboard/api/auth-type/" + current_user.username + "@yopmail.com/" + current_user.password_hash
        x = requests.get(link)
        data = json.loads(x.text)
        if(data['authType'] != 'IP' or data['ipAuthType'] != 'SOCKS'):
            print("i'm in")
            link = "https://blazingseollc.com/proxy/dashboard/api/auth-type/" + current_user.username + "@yopmail.com/" + current_user.password_hash +"/IP?ipAuthType=SOCKS"
        print(link)
        x = requests.get(link)
        print(x.text)
        if form.choice.data == 'auth':
            addIP(form.ip.data, current_user.username, current_user.password_hash)
        elif form.choice.data == 'deauth':
            removeIP(form.ip.data, current_user.username, current_user.password_hash)
        flash('Updated!')
        return redirect(url_for('users.authenticateip'))

    return render_template('authenticateip.html', form=form)
