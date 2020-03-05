import os
import functools
from flask import session
from flask import render_template
from flask import send_from_directory
from flask import Blueprint
from flask import redirect

bp = Blueprint("index", __name__, url_prefix="")


@bp.route('/')
def jumpto():
    return 'index page'


@bp.route('/<path:_file>')
def favicon(_file):
    return send_from_directory(os.path.join(bp.root_path, '../static'), _file)


@bp.errorhandler(404)
def errer_500(e):
    return render_template('404.html')


def if_superuser(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('superuser') is False:
            return render_template('permission.html')

        return view(**kwargs)

    return wrapped_view
