from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required

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
@login_required
def index():
    """Exibe todos os autores cadastrados, ordem decrescente"""
    try:
        autores = db.query_bd('select * from autor')
        return render_template('autor/index.html', autores=autores)
    except:
        return render_template('404.html')


@bp.route('/autor/create', methods=('GET', 'POST'))
@login_required
def create():
    """Cria um novo autor."""
    error = None
    if request.method == 'POST':
        nome = request.form['nome']
        if not nome:
            error = 'Nome é obrigatório.'
        else:
            try:
                if verifica_autor_bd(nome):
                    error = 'Autor já cadastrado!'
                else:
                    db.insert_bd('INSERT INTO autor values (default, "%s")' % nome)
                    return redirect(url_for('autor.index'))
            except Exception as e:
                print(e)
                return redirect(url_for('error'))

    return render_template('autor/create.html', error=error)


def verifica_autor_bd(nome):
    autor = db.query_bd('SELECT * FROM autor WHERE nome = "%s"' % nome)
    if autor:
        return True
    return False


@bp.route('/autor/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Atualiza um autor pelo seu respectivo id."""
    autor = get_autor(id)
    error = None
    if request.method == 'POST':
        nome = request.form['nome']

        if not nome:
            error = 'Nome é obrigatório.'
        print(autor)
        if nome == autor['nome']:
            return redirect(url_for('autor.index'))

        else:
            try:
                if verifica_autor_bd(nome):
                    error = 'Este autor já está registrado!'
                else:
                    db.insert_bd('UPDATE autor set nome = "%s" where id = %d' % (nome, id))
                    return redirect(url_for('autor.index'))
            except:
                return render_template('404.html')

    return render_template('autor/update.html', autor=autor, error=error)


@bp.route('/autor/<int:id>/delete', methods=('POST',))
@login_required
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
