import functools
from flask import session
from flask import render_template


def if_superuser(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('superuser') is False:
            return render_template('permission.html')

        return view(**kwargs)

    return wrapped_view
