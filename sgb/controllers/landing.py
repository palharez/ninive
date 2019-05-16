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
            inner join socio on emprestimo.id_socio = socio.id;')
        reservas = db.query_bd('select * from reserva inner join livro on reserva.tombo = livro.tombo inner join socio on reserva.id_socio = socio.id;')
        return render_template('landing/index.html', livros=livros, emprestimos=emprestimos, reservas=reservas)
    except:
        return render_template('404.html')
