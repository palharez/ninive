import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required

bp = Blueprint('livro', __name__)

def parse_request(request):
    return {
        'id_autor': int(request.form['autor']),
        'id_editora': int(request.form['editora']),
        'titulo': request.form['titulo'],
        'tombo': int(request.form['tombo']),
        'entrada': request.form['entrada'],
        'etiqueta': request.form['etiqueta'],
        'ano': int(request.form['ano']),
        'exemplar': int(request.form['exemplar']),
        'volume': request.form['volume']
    }


def get_livro(id):
    try:
        livro = db.query_one('select * from livro where tombo = %d' % id)

        if livro is None:
            return render_template('404.html')

        return livro
    except:
        return render_template('404.html')


@bp.route('/livro/get_nome/<int:tombo>', methods=('GET',))
def get_nome(tombo):
    """pega o nome de um livro pelo tombo."""

    if request.method == 'GET':
        try:            
            livro = get_livro(tombo)
            content = {
                'titulo': livro['titulo'],
                'status': livro['status']
            }
            return json.dumps(content)
        except Exception as e:
            print(e)
            return render_template('404.html')


@bp.route('/livro')
@login_required
def index():
    """Exibe todas as livros cadastradas."""
    try:
        livros = db.query_bd('select * from livro inner join autor on autor.id = livro.id_autor inner join editora on editora.id = livro.id_editora; ')
        return render_template('livro/index.html', livros=livros)
    except Exception as e:
        print(e)
        return render_template('404.html')


@bp.route('/livro/create', methods=('GET', 'POST'))
@login_required
def create():
    """Cria um novo livro."""
    editoras = db.query_bd('select * from editora')
    autores = db.query_bd('select * from autor')

    if request.method == 'POST':
        try:
            request_parsed = parse_request(request)
            print(request_parsed['entrada'])
            sql = 'INSERT INTO livro values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", default)' % (request_parsed['tombo'], 
                request_parsed['titulo'], request_parsed['entrada'], request_parsed['etiqueta'], request_parsed['ano'], 
                request_parsed['volume'], request_parsed['exemplar'], request_parsed['id_editora'], request_parsed['id_autor'])
            print(sql)
            db.insert_bd(sql)
            return redirect(url_for('livro.index'))
        except Exception as e:
            print(e)
            return render_template('404.html')


    return render_template('livro/create.html', livro_content={'editoras': editoras, 'autores': autores})

@bp.route('/livro/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Atualiza um livro pelo seu respectivo id."""
    livro = get_livro(id)
    editoras = db.query_bd('select * from editora')
    autores = db.query_bd('select * from autor')
    print(livro)

    if request.method == 'POST':
        request_parsed = parse_request(request)
        try:
            sql = 'UPDATE livro set titulo = "%s", entrada = "%s", etq = "%s", ano = "%s", ex = "%s", v = "%s", id_editora = "%s", id_autor = "%s" where tombo = %d' % (request_parsed['titulo'], request_parsed['entrada'], request_parsed['etiqueta'], request_parsed['ano'], request_parsed['exemplar'], request_parsed['volume'], request_parsed['id_editora'], request_parsed['id_autor'], request_parsed['tombo'])
            print(sql)
            db.insert_bd(sql)
            return redirect(url_for('livro.index'))
        except:
            return render_template('404.html')

    return render_template('livro/update.html', livro_content={'editoras': editoras, 'autores': autores, 'livro': livro})


@bp.route('/livro/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    """Deleta um livro.

   Certifica que o livro existe.
    """
    
    try:
        get_livro(id)

        db.insert_bd('DELETE FROM livro WHERE tombo = %d' % id)
        return redirect(url_for('livro.index'))
    except Exception as e:
        print(e)
        return render_template('404.html')


@bp.route('/livro/update_status', methods=('GET', 'POST'))
@login_required
def update_status():
    """Atualiza o status do livro."""
    
    if request.method == 'POST':
        try:
            status = request.form['status']
            tombo = request.form['tombos']
            sql = 'UPDATE livro SET status = "%s" WHERE tombo = "%s" ' % (status, tombo)
            db.insert_bd(sql)
            return redirect(url_for('livro.index'))
        except Exception as e:
            return render_template('404.html')

    sql = 'select tombo, status from livro'
    livros = db.query_bd(sql)

    return render_template('livro/update_status.html', livros=livros)
