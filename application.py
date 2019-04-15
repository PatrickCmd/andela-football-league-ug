import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config.get(config_name, 'default'))

    # setup_db
    db.init_app(app)

    # import blueprints
    from home.views import home
    from person.views import person_app
    from team.views import team_app

    # register blueprints
    app.register_blueprint(home)
    app.register_blueprint(team_app)
    app.register_blueprint(person_app)

    return app
