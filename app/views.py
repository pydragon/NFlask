__author__ = 'yangziling'
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    #user = {'nickname':'Miguel'} # fake user
    user = g.user
    posts = [
        {
            'author' :{'nickname':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname':'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title = 'MyHome',
                           user = user,
                           posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
#@oid.loginhandler
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #flash('Login requested for OpenID = "' + form.openid.data + '", remember_me ' + str(form.remember_me.data))
        #return redirect('/index')
        session['remember_me'] = form.remember_me.data
        print form.openid.data
        app.logger.info('LoginUser Info: ' + form.openid.data)
        user = User.query.filter_by(nickname=form.openid.data).first()
        if user is not None:
            g.user = user
            login_user(user)
            #return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
            return redirect(url_for('index'))
        else:
            flash('User <' + form.openid.data + '> is invalidated, pls. input the correct User Account! ')
    return render_template('login.html',
                            title = 'Sign In',
                            form = form,
                            providers = app.config['OPENID_PROVIDERS'])


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@oid.after_login
def after_login(resp):
    print 'come to afterlogin----'
    print resp
    if resp.email is None or resp.email == "":
        flash('Invalid lgin. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname == resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    print 'return afterlogin-----'
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname = nickname).first()
    if user == None:
        flash('User ' + nickname + 'not found.')
        return redirect(url_for('index'))
    posts = [
        {'author':user, 'body':'Test post #1'},
        {'author':user, 'body':'Test post #2'}
    ]
    return render_template('user.html', user = user, posts = posts)

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500



