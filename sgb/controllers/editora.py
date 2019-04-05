from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db

bp = Blueprint('editora', __name__)


def get_editora(id):
    try:
        editora = db.query_one('select * from editora where id = %d' % id)

        if editora is None:
            return render_template('404.html')

        return editora
    except:
        return render_template('404.html')

@bp.route('/editora')
def index():
    """Exibe todas as editoras cadastradas."""
    try:
        editoras = db.query_bd('select * from editora')
        return render_template('editora/index.html', editoras=editoras)
    except:
        return render_template('404.html')


@bp.route('/editora/create', methods=('GET', 'POST'))
def create():
    """Cria uma nova editora."""
    if request.method == 'POST':
        nome = request.form['nome']
        error = None

        if not nome:
            error = 'Nome é obrigatório.'

        if error is not None:
            flash(error)
            
        else:

            try:
                db.insert_bd('INSERT INTO editora values (default, "%s")' % nome)
                return redirect(url_for('editora.index'))
                
            except:
                return render_template('404.html')

    return render_template('editora/create.html')

@bp.route('/editora/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    """Atualiza uma editora pelo seu respectivo id."""
    editora = get_editora(id)
    if request.method == 'POST':
        nome = request.form['nome']
        error = None

        if not nome:
            error = 'Nome é obrigatório.'

        if error is not None:
            flash(error)
        
        else:
            try:
                db.insert_bd('UPDATE editora set nome = "%s" where id = %d' % (nome, id))
                return redirect(url_for('editora.index'))
            except:
                return render_template('404.html')

    return render_template('editora/update.html', editora=editora)

@bp.route('/editora/<int:id>/delete', methods=('POST',))
def delete(id):
    """Deleta um autor.

   Certifica que o autor existe.
    """
    get_editora(id)
    try:
        db.insert_bd('DELETE FROM  editora WHERE id = %d' % id)
        return redirect(url_for('editora.index'))
    except:
        return render_template('404.html')
