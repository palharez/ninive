from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required

bp = Blueprint('reserva', __name__)


def get_reserva(id):
    try:
        reserva = db.query_one('select * from reserva where id = %d' % id)

        if reserva is None:
            return render_template('404.html')

        return reserva
    except:
        return render_template('404.html')


@bp.route('/reserva', defaults={'page': 1}, methods=('GET', 'POST'))
@bp.route('/socio/page/<int:page>')
@login_required
def index(page):
    """Exibe todos as emprstimos cadastradas."""
    try:
        perpage = 12
        startat = ( page - 1 ) * perpage
        perpage *= page
        totalreserva = db.query_bd('select * from reserva \
            inner join livro on reserva.tombo = livro.tombo \
            inner join socio on reserva.id_socio = socio.id;')
        totalpages = int(len(totalreserva) / 12) + 1 
        if request.method == 'POST':
            busca = request.form['busca']
            tipo = request.form['tipo']
            if tipo == "tombo":
                sql = "SELECT reserva.*,  \
                    (SELECT s.nome FROM socio s WHERE s.id = reserva.id_socio) as 'nome', \
                    (SELECT l.titulo FROM livro l WHERE l.tombo = reserva.tombo) as 'titulo' \
                    FROM reserva \
                    WHERE reserva.tombo \
                    LIKE '%{}%' limit {}, {};".format(busca, startat, perpage)
            elif tipo == "nome":
                sql = "SELECT reserva.*,  \
                    (SELECT s.nome FROM socio s WHERE s.id = reserva.id_socio) as 'nome', \
                    (SELECT l.titulo FROM livro l WHERE l.tombo = reserva.tombo) as 'titulo' \
                    FROM reserva \
                    WHERE (SELECT s.nome FROM socio s WHERE s.id = reserva.id_socio) \
                    LIKE '%{}%' limit {}, {};".format(busca, startat, perpage)
            reservas = db.query_bd(sql)
            print(reservas)
            totalpages = int(len(reservas) / 12) + 1 
        else:
            reservas = db.query_bd('select * from reserva \
            inner join livro on reserva.tombo = livro.tombo \
            inner join socio on reserva.id_socio = socio.id limit %s, %s;' % (startat, perpage))
        reservas = reservas[:12]
        return render_template('reserva/index.html', reservas=reservas, page=page, totalpages=totalpages)
    except Exception as e:
        print(e)
        return render_template('404.html')


@bp.route('/reserva/create', methods=('GET', 'POST'))
@login_required
def create():
    """
    Reserva um livro.
    
    Verificar se o livro já não foi reservado.
    """
    data = {
        'error': '',
        'livro': '',
        'socio': ''
    }
    success = False
    try:
        socios_id = db.query_bd('select id from socio order by id')
        livros_tombo = db.query_bd('select tombo from livro order by tombo')
    except Exception as e:
        print(e)
        return render_template('404.html')

    if request.method == 'POST':
        try:
            idsocio = request.form['idsocio']
            tombo = request.form['tombo']

            data['livro'] = livro = db.query_one('select * from livro where tombo = %s' % tombo)
            data['socio'] = socio = db.query_one('select * from socio where id = %s' % idsocio)

            qtdlivro = livro['qtd']

            if qtdlivro <= 0:
                data['error'] = 'Este livro não está disponível!'

            elif data['socio']['status'] == 'SUSPENSO':
                data['error'] = 'Não é possível criar reserva pois o sócio está suspenso!'

            elif livro['status'] == 'ESTANTE':
                qtdlivro -= 1
                reservar_livro(tombo, idsocio, qtdlivro)
                success = True

            elif livro['status'] == 'EMPRESTADO':
                data['error'] = 'Este livro não pode ser reservado! ' \
                    'Pois já está emprestado.'

            elif livro['status'] == 'PERDIDO':
                data['error'] = 'Este livro não pode ser reservado! ' \
                    'Pois está perdido.'
                    
            elif livro['status'] == 'EXTRAVIADO':
                data['error'] = 'Este livro não pode ser reservado! ' \
                    'Pois está extraviado.'

            elif livro['status'] == 'RESERVADO':
                reserva = db.query_one('select * from reserva where tombo = %s and id_socio = %s' % (tombo, idsocio))
                if reserva:
                    data['error'] = 'Este livro não pode ser reservado! ' \
                        'Pois já está reservado.'
                else:
                    qtdlivro -= 1
                    reservar_livro(tombo, idsocio, qtdlivro)
                    success = True

        except Exception as e:
            print(e)
            return render_template('404.html')

    return render_template('reserva/create.html', data=data, success=success, socios_id=socios_id, livros_tombo=livros_tombo)


def reservar_livro(tombo, idsocio, qtdlivro):
    db.insert_bd('UPDATE livro SET qtd = "%s" WHERE tombo = "%s" ' % (qtdlivro, tombo))
    sql = "insert into reserva values(default, default, '%s', '%s')" % (tombo, idsocio)
    db.insert_bd(sql)
    if qtdlivro == 0:
        db.insert_bd('UPDATE livro SET status = "Reservado" WHERE tombo = "%s" ' % tombo)


@bp.route('/reserva/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    """Deleta uma reserva.

   Certifica que a reserva existe.
   Atualiza o status do livro para estante
    """
    reserva = get_reserva(id)
    try:
        livro = db.query_one('select * from livro where tombo = %s' % reserva['tombo'])
        qtdlivro = livro['qtd']
        qtdlivro += 1
        db.insert_bd('UPDATE livro SET status = "ESTANTE", qtd = "%s" WHERE tombo = "%s" ' % (qtdlivro, reserva['tombo']))
        db.insert_bd('DELETE FROM reserva WHERE id = %d' % id)
        return redirect(url_for('reserva.index'))
    except Exception as e:
        print(e)
        return render_template('404.html')


@bp.route('/reserva/<int:id>/emprestimo', methods=('GET',))
@login_required
def emprestimo(id):
    """
    Deleta uma reserva e gera um empréstimo.

    Certifica que a reserva existe.
    Atualiza o status do livro para emprestado
    """
    reserva = get_reserva(id)
    try:
        livro = db.query_one('select * from livro where tombo = %s' % reserva['tombo'])
        print(livro)
        qtdlivro = livro['qtd']
        if qtdlivro != 0:
            qtdlivro -= 1
        db.insert_bd('UPDATE livro SET qtd = "%s" WHERE tombo = "%s" ' % (qtdlivro, reserva['tombo']))
        if qtdlivro == 0:
            db.insert_bd('UPDATE livro SET status = "EMPRESTADO" WHERE tombo = "%s" ' % reserva['tombo'])
        db.insert_bd('DELETE FROM reserva WHERE id = %d' % id)
        sql = "insert into emprestimo values(default, date_format(now(), '%%Y-%%m-%%d'), DATE_ADD(CURDATE(), INTERVAL 5 DAY), '%s', '%s')" % (reserva['tombo'], reserva['id_socio'])
        db.insert_bd(sql)
        return redirect(url_for('reserva.index'))
    except Exception as e:
        print(e)
        return render_template('404.html')    