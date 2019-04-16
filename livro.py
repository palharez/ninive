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
        'nomenclatura': request.form['nomenclatura'],
        'volume': request.form['volume']
    }



@bp.route('/livro')
@login_required
def index():
    """Exibe todas as livros cadastradas."""
    try:
        livros = db.query_bd('select * from livro inner join autor on autor.id = livro.id_autor inner join editora on editora.id = livro.id_edtora; ')
        return render_template('livro/index.html', livros=livros)
    except:
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
            sql = 'INSERT INTO livro values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", default ,"%s")' % (request_parsed['tombo'], 
                request_parsed['titulo'], request_parsed['entrada'], request_parsed['etiqueta'], request_parsed['ano'], 
                request_parsed['volume'], request_parsed['exemplar'], request_parsed['id_autor'], request_parsed['id_editora'], 
                request_parsed['nomenclatura'])
            db.insert_bd(sql)
            return redirect(url_for('livro.index'))
        except Exception as e:
            return render_template('404.html')


    return render_template('livro/create.html', livro_content={'editoras': editoras, 'autores': autores})
