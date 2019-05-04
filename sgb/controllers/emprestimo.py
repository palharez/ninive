from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required

bp = Blueprint('emprestimo', __name__)


def get_emprestimo(id):
    try:
        emprestimo = db.query_one('select * from emprestimo where id = %d' % id)

        if emprestimo is None:
            return render_template('404.html')

        return emprestimo
    except:
        return render_template('404.html')


@bp.route('/emprestimo', methods=('GET',))
@login_required
def index():
    """Exibe todos as emprstimos cadastradas."""
    try:
        emprestimos = db.query_bd('select * from emprestimo \
            inner join livro on emprestimo.tombo = livro.tombo \
            inner join socio on emprestimo.id_socio = socio.id;')
        print(emprestimos)
        return render_template('emprestimo/index.html', emprestimos=emprestimos)
    except Exception as e:
        print(e)
        return render_template('404.html')


@bp.route('/emprestimo/create', methods=('GET', 'POST'))
@login_required
def create():
    """Cria um novo emprestimo."""
    if request.method == 'POST':
        try:
            db.insert_bd('INSERT INTO emprestimo values (default, "%s")' % nome)
            return redirect(url_for('emprestimo.index'))
                
        except:
            return render_template('404.html')

    return render_template('emprestimo/create.html')


@bp.route('/emprestimo/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Atualiza uma emprestimo pelo seu respectivo id."""
    emprestimo = get_emprestimo(id)
    if request.method == 'POST':
        try:
            db.insert_bd('UPDATE emprestimo set nome = "%s" where id = %d' % (nome, id))
            return redirect(url_for('emprestimo.index'))
        except:
            return render_template('404.html')

    return render_template('emprestimo/update.html', emprestimo=emprestimo)


@bp.route('/emprestimo/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    """Deleta um empretimo.

   Certifica que o emprestimo existe.
    """
    get_emprestimo(id)
    try:
        db.insert_bd('DELETE FROM  emprestimo WHERE id = %d' % id)
        return redirect(url_for('emprestimo.index'))
    except:
        return render_template('404.html')
