import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required

bp = Blueprint('socio', __name__)


def parse_request(request):
    return {
        'nome': request.form['nome'],
        'rg': int(request.form['rg']),
        'nasc': request.form['nasc'],
        'email': request.form['email'],
        'nome_pai': request.form['nome_pai'],
        'nome_mae': request.form['nome_mae'],
        'cidade': request.form['cidade'],
        'bairro': request.form['bairro'],
        'logradouro': request.form['logradouro'],
        'num': int(request.form['numero']),
        'tel_res': int(request.form['tel_res']),
        'cel_1': int(request.form['cel_1']),
        'cel_2': int(request.form['cel_2'])
    }

def get_socio(id):
    try:
        socio = db.query_one('select * from socio where id = %d' % id)

        if socio is None:
            return render_template('404.html')

        return socio
    except:
        return render_template('404.html')


@bp.route('/socio')
@login_required
def index():
    """Exibe todos os socios cadastrados."""
    try:
        socios = db.query_bd('select * from socio')
        return render_template('socio/index.html', socios=socios)
    except:
        return render_template('404.html')


@bp.route('/socio/create', methods=('GET', 'POST'))
@login_required
def create():
    """Cria um novo socio."""

    if request.method == 'POST':
        try:
            request_parsed = parse_request(request)
            sql = 'INSERT INTO socio values (default, "%s", "%s", "%s", "%s", default, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (request_parsed['nome'], 
                request_parsed['rg'], request_parsed['nasc'], request_parsed['email'], request_parsed['nome_pai'], 
                request_parsed['nome_mae'], request_parsed['cidade'], request_parsed['bairro'], request_parsed['logradouro'], 
                request_parsed['num'], request_parsed['tel_res'], request_parsed['cel_1'], request_parsed['cel_2'])
            db.insert_bd(sql)
            return redirect(url_for('socio.index'))
        except Exception as e:
            print(e)
            return render_template('404.html')

    return render_template('socio/create.html')

@bp.route('/socio/<int:id>', methods=('GET',))
@login_required
def verifica(id):
    """Retorna um único sócio para verificação de todos os dados"""
    try:
        socio = get_socio(id)
        print(id)
        print(socio)
        return render_template('socio/verifica.html', socio=socio)
    except Exception as e:
        print(e)
        return render_template('404.html')

