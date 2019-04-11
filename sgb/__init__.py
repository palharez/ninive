import os

from flask import Flask, g
from sgb.database import Database

# Setando db como global
db = Database()


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    @app.route('/hello')
    def hello():
        return 'Hello'

    from sgb.controllers import autor, editora
    app.register_blueprint(autor.bp)
    app.register_blueprint(editora.bp)

    return app
