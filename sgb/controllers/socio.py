import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required
from sgb.utils import upload_file

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
        'cel_2': int(request.form['cel_2']) or ''
    }


def get_socio(id):
    """Retorna um sócio de acordo com seu id"""
    socio = db.query_one('select * from socio where id = %d' % id)

    if socio is None:
        raise Exception('Não encontrouo socio com o id %d' % id)

    return socio


@bp.route('/socio/nome/<int:id>/emprestimo', methods=('GET',))
def get_nome(id):
    """Pega o nome de um socio pelo id."""

    if request.method == 'GET':
        try:            
            socio = get_socio(id)
            return json.dumps({ 'nome': socio['nome'] })
        except Exception as e:
            return json.dumps({ 'msg': 'Sócio não encontrado' })


@bp.route('/socio', defaults={'page': 1}, methods=('GET', 'POST'))
@bp.route('/socio/page/<int:page>')
@login_required
def index(page):
    """Exibe todos os socios cadastrados."""
    try:
        perpage = 12
        startat = ( page - 1 ) * perpage
        perpage *= page
        totalsocio = db.query_bd('select * from socio')
        totalpages = int(len(totalsocio) / 12) + 1 
        if request.method == 'POST':
            busca = request.form['busca']
            tipo = request.form['tipo']
            sql = "SELECT * FROM socio WHERE {} LIKE '%{}%' limit {}, {};".format(tipo, busca, startat, perpage)
            socios = db.query_bd(sql)
            totalpages = int(len(socios) / 12) + 1 
        else:
            socios = db.query_bd('select * from socio limit %s, %s;' % (startat, perpage))
        socios = socios[:12]
        return render_template('socio/index.html', socios=socios, page=page, totalpages=totalpages)
    except Exception as e:
        print(e)
        return render_template('404.html')


@bp.route('/socio/create', methods=('GET', 'POST'))
@login_required
def create():
    """Cria um novo socio."""

    if request.method == 'POST':
        try:
            request_parsed = parse_request(request)
            f = ""
            if request.files['image']:
                file = request.files['image']
                f = upload_file(file)
            name_image = f.filename if f else 'who.png'
            sql = 'INSERT INTO socio values (default, "%s", "%s", "%s", "%s", default, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (request_parsed['nome'],
                                                                                                                                                 request_parsed['rg'], request_parsed['nasc'], request_parsed[
                                                                                                                                                     'email'], request_parsed['nome_pai'],
                                                                                                                                                 request_parsed['nome_mae'], request_parsed['cidade'], request_parsed[
                                                                                                                                                     'bairro'], request_parsed['logradouro'],
                                                                                                                                                 request_parsed['num'], request_parsed['tel_res'], request_parsed['cel_1'], request_parsed['cel_2'], name_image)

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
        return render_template('socio/verifica.html', socio=socio)
    except Exception as e:
        return render_template('404.html')


@bp.route('/socio/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Faz o update do sócio informado pelo id"""
    try:
        socio = get_socio(id)

        if request.method == 'POST':
            f = ""
            if request.files['image']:
                file = request.files['image']
                f = upload_file(file)
            name_image = f.filename if f else socio['caminho_imagem']
            request_parsed = parse_request(request)
            sql = 'UPDATE socio set nome = "%s", rg = "%s", nasc = "%s", email = "%s", nome_pai = "%s", nome_mae = "%s", cidade = "%s", bairro = "%s", logradouro = "%s", num = "%s", tel_res = "%s", cel_1 = "%s", cel_2 = "%s", caminho_imagem = "%s" where id = %d' % (request_parsed['nome'], request_parsed['rg'], request_parsed['nasc'], request_parsed['email'], request_parsed['nome_pai'], request_parsed['nome_mae'], request_parsed['cidade'], request_parsed['bairro'], request_parsed['logradouro'], request_parsed['num'], request_parsed['tel_res'], request_parsed['cel_1'], request_parsed['cel_2'], name_image, id)
            db.insert_bd(sql)
            return redirect(url_for('socio.index'))

        return render_template('socio/update.html', socio=socio)

    except Exception as e:
        print(e)
        return render_template('404.html')


@bp.route('/socio/<int:id>/delete', methods=('GET',))
@login_required
def delete(id):
    """Deleta um socio de acordo com seu id"""
    try:
        socio = get_socio(id)
        sql = 'DELETE from socio where id = %d' % id
        db.insert_bd(sql)
        return redirect(url_for('socio.index'))
    except Exception as e:
        print(e)
        return render_template('404.html')
    