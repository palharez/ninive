import os

from flask import Flask, g
from sgb.database import Database

db = {}

# Setando db como global
def db_app(dbname):
    global db
    db = Database(dbname)


def create_app(dbname='TCC'):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    db_app(dbname)

    @app.route('/hello')
    def hello():
        return 'Hello'

    @app.route('/500')
    def error():
        return 'Erro 500', 500

    from sgb.controllers import autor, editora, funcionario

    app.register_blueprint(funcionario.bp)
    app.register_blueprint(autor.bp)
    app.register_blueprint(editora.bp)

    return app
