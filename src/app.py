import os
import datetime

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
import setting

__version__ = (1, 0, 0, "dev")

db = SQLAlchemy()


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    # some deploy systems set the database url in the environ
    db_url = setting.DATABASE_URL

    if db_url is None:
        # default to a sqlite database in the instance folder
        db_url = "sqlite:///" + os.path.join(app.instance_path, "test.sqlite")
        # ensure the instance folder exists
        os.makedirs(app.instance_path, exist_ok=True)

    app.config.from_mapping(
        # default secret that should be overridden in environ or config
        PERMANENT_SESSION_LIFETIME=datetime.timedelta(hours=10),
        UPLOAD_FOLDER=setting.UPLOAD_FOLDER,
        MAX_CONTENT_LENGTH=setting.MAX_CONTENT_LENGTH,
        SECRET_KEY=setting.SECRET_KEY,
        SQLALCHEMY_DATABASE_URI=db_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # initialize Flask-SQLAlchemy and the init-db command
    db.init_app(app)

    # apply the blueprints to the app
    import auth
    import models
    import views

    app.register_blueprint(auth.bp)
    app.register_blueprint(views.index_views)

    # make "index" point at "/", which is handled by "blog.index"
    # app.add_url_rule("/", view_func=common.jumpto)

    return app


def init_db():
    if setting.dev:
        db.drop_all()
    db.create_all()
    from auth.models import User
    for d in setting.users_list:
        User().save(d)
    click.echo('create users finish !')

    from models import Saler
    salers = ['salers']
    for saler in salers:
        Saler().save(saler)
    click.echo('create saler finish !')
    click.echo("Initialized the database.")


@click.command("init")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    from common.alter_table import alter_table
    alter_table()

