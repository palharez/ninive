import os

from flask import Flask, g
from sgb.database import Database
from flask_cors import CORS

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

    CORS(app)

    db_app(dbname)

    @app.route('/hello')
    def hello():
        return 'Hello'

    from sgb.controllers import autor, editora, funcionario, livro, landing, socio, emprestimo

    app.register_blueprint(funcionario.bp)
    app.register_blueprint(autor.bp)
    app.register_blueprint(editora.bp)
    app.register_blueprint(livro.bp)
    app.register_blueprint(landing.bp)
    app.register_blueprint(socio.bp)
    app.register_blueprint(emprestimo.bp)

    return app
