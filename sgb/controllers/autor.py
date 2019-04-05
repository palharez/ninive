from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db

bp = Blueprint('autor', __name__)


def get_autor(id):
    try:
        autor = db.query_one('select * from autor where id = %d' % id)

        if autor is None:
            return render_template('404.html')

        return autor
    except:
        return render_template('404.html')

@bp.route('/autor')
def index():
    """Exibe todos os autores cadastrados, ordem decrescente"""
    try:
        autores = db.query_bd('select * from autor')
        return render_template('autor/index.html', autores=autores)
    except:
        return render_template('404.html')


@bp.route('/autor/create', methods=('GET', 'POST'))
def create():
    """Cria um novo autor."""
    if request.method == 'POST':
        nome = request.form['nome']
        error = None

        if not nome:
            error = 'Nome é obrigatório.'

        if error is not None:
            flash(error)
            
        else:

            try:
                db.insert_bd('INSERT INTO autor values (default, "%s")' % nome)
                return redirect(url_for('autor.index'))
                
            except:
                return render_template('404.html')

    return render_template('autor/create.html')


@bp.route('/autor/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    """Atualiza um autor pelo seu respectivo id."""
    autor = get_autor(id)
    if request.method == 'POST':
        nome = request.form['nome']
        error = None

        if not nome:
            error = 'Nome é obrigatório.'

        if error is not None:
            flash(error)
        
        else:
            try:
                db.insert_bd('UPDATE autor set nome = "%s" where id = %d' % (nome, id))
                return redirect(url_for('autor.index'))
            except:
                return render_template('404.html')

    return render_template('autor/update.html', autor=autor)


@bp.route('/autor/<int:id>/delete', methods=('POST',))
def delete(id):
    """Deleta um autor.

   Certifica que o autor existe.
    """
    get_autor(id)
    try:
        db.insert_bd('DELETE FROM  autor WHERE id = %d' % id)
        return redirect(url_for('autor.index'))
    except:
        return render_template('404.html')
