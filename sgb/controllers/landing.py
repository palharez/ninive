from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required

bp = Blueprint('landing', __name__)


@bp.route('/landing')
@login_required
def index():
    """Exibe a landing page."""
    try:
        livros = db.query_bd('select * from livro inner join autor on autor.id = livro.id_autor inner join editora on editora.id = livro.id_editora limit 4; ')
        emprestimos = emprestimos = db.query_bd('select * from emprestimo \
            inner join livro on emprestimo.tombo = livro.tombo \
            inner join socio on emprestimo.id_socio = socio.id limit 4;')
        reservas = db.query_bd('select * from reserva inner join livro on reserva.tombo = livro.tombo inner join socio on reserva.id_socio = socio.id limit 4;')
        total = db.query_bd('SELECT count(tombo)as "qnt" FROM livro;')
        emprestado = db.query_bd('SELECT count(tombo)as "qnt" FROM livro WHERE status = "emprestado";')
        reservado = db.query_bd('SELECT count(tombo)as "qnt" FROM livro WHERE status = "reservado";')
        estante = db.query_bd('SELECT count(tombo)as "qnt" FROM livro WHERE status = "estante";')

        return render_template('landing/index.html', livros=livros, emprestimos=emprestimos, reservas=reservas,
         total=total, reservado=reservado, emprestado=emprestado, estante=estante)
    except:
        return render_template('404.html')
