import time
import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_login import login_required

from app import db
from setting import logger, dev
from .models import User
from common import send_mail

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/")
@login_required
def index():
    return redirect(url_for("/project/list"))


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")
    g.user = User.query.get(user_id) if user_id is not None else None


# @bp.route("/register", methods=("GET", "POST"))
# def register():
# """Register a new user.

# Validates that the username is not already taken. Hashes the
# password for security.
# """
# if request.method == "POST":
# username = request.form["username"]
# password = request.form["password"]
# error = None

# if not username:
# error = "Username is required."
# elif not password:
# error = "Password is required."
# elif db.session.query(
# User.query.filter_by(username=username).exists()).scalar():
# error = f"User {username} is already registered."

# if error is None:
# the name is available, create the user and go to the login page
# db.session.add(User(username=username, password=password))
# db.session.commit()
# return redirect(url_for("auth.login"))

# flash(error)

# return render_template("auth/register.html")


@bp.route("/login/", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form.get("password")
        verification_code = request.form.get('verification_code')
        logger.info('%s %s %s' % (username, password, verification_code))
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = {'danger': '用户名不存在!'}
        elif password:
            if not user.check_password(password):
                error = {'danger': "用户名/密码不正确!"}

            if dev and error is None:
                return login_success(user)

            if error is None:
                # store the user id in a new session and return to the index
                code = str(time.time()).split('.')[-1]
                user.code = code
                db.session.commit()
                logger.info(f'{username} {code}')
                send_mail(code, username)
                return render_template('auth/confirm.html', username=username)

        elif verification_code:
            if not user.check_code(verification_code):
                error = {'danger': "验证码不正确!"}

            if error is None:
                return login_success(user)

        logger.info(error)
        flash(error)

    return render_template("auth/login.html", messages=error)


def login_success(user):
    session.clear()
    session["user_id"] = user.id
    session["superuser"] = user.superuser
    session.permanent = True
    return redirect('/project/list')


@bp.route("/update/", methods=("GET", "POST"))
def update():
    user = User.query.filter_by(id=session['user_id']).first()
    if request.method == "GET":
        return render_template('auth/update.html', username=user.username)
    elif request.method == "POST":
        user._password = request.form['password']
        db.session.commit()
        logger.info('user password update success %s' % user.username)
        return redirect('/project/list')
    else:
        return redirect('/project/list')


@bp.route("/logout/")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect('/project/list')
