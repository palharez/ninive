from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required

bp = Blueprint('editora', __name__)


def get_editora(id):
    try:
        editora = db.query_one('select * from editora where id = %d' % id)

        if editora is None:
            return render_template('404.html')

        return editora
    except:
        return render_template('404.html')

@bp.route('/editora', defaults={'page': 1}, methods=('GET', 'POST'))
@bp.route('/editora/page/<int:page>')
@login_required
def index(page):
    """Exibe todas as editoras cadastradas."""
    try:
        perpage = 9
        startat = ( page - 1 ) * perpage
        perpage *= page
        totaleditoras = db.query_bd('select * from editora')
        totalpages = int(len(totaleditoras) / 9) + 1
        if request.method == 'POST':
            busca = request.form['busca']
            tipo = request.form['tipo']
            sql = "SELECT * FROM editora WHERE {} LIKE '%{}%' limit {}, {};".format(tipo, busca, startat, perpage)
            editoras = db.query_bd(sql)
            totalpages = int(len(editoras) / 9) + 1 
        else:
            editoras = db.query_bd('select * from editora limit %s, %s;' % (startat, perpage))
        editoras = editoras[:9]
        return render_template('editora/index.html', editoras=editoras, page=page, totalpages=totalpages)
    except:
        return render_template('404.html')


@bp.route('/editora/create', methods=('GET', 'POST'))
@login_required
def create():
    """Cria uma nova editora."""
    error = None
    success = False
    if request.method == 'POST':
        nome = request.form['nome']
        error = None

        if not nome:
            error = 'Nome é obrigatório.'
        else:
            try:
                if verifica_editora_bd(nome):
                    error = 'Editora já cadastrada!'
                else:
                    db.insert_bd('INSERT INTO editora values (default, "%s")' % nome)
                    success = True
            except:
                return render_template('404.html')

    return render_template('editora/create.html', error=error, success=success)

def verifica_editora_bd(nome):
    editora = db.query_bd('SELECT * FROM editora WHERE nome = "%s"' % nome)
    if editora:
        return True
    return False


@bp.route('/editora/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Atualiza uma editora pelo seu respectivo id."""
    editora = get_editora(id)
    error = None
    if request.method == 'POST':
        nome = request.form['nome']
        error = None

        if not nome:
            error = 'Nome é obrigatório.'
        if nome == editora['nome']:
            return redirect(url_for('editora.index'))

        else:
            try:
                if verifica_editora_bd(nome):
                    error = 'Essa editora já está registrada!'
                else:
                    db.insert_bd('UPDATE editora set nome = "%s" where id = %d' % (nome, id))
                    return redirect(url_for('editora.index'))
            except:
                return render_template('404.html')

    return render_template('editora/update.html', editora=editora, error=error)

@bp.route('/editora/<int:id>/delete', methods=('POST',))
@login_required
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
