from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required

bp = Blueprint('emprestimo', __name__)


def get_emprestimo(id):
    try:
        emprestimo = db.query_one(
            'select * from emprestimo where id = %d' % id)

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
        return render_template('emprestimo/index.html', emprestimos=emprestimos)
    except Exception as e:
        print(e)
        return render_template('404.html')


@bp.route('/emprestimo/create', methods=('GET', 'POST'))
@login_required
def create():
    """Cria um novo emprestimo."""
    data = {
        'error': '',
        'livro': '',
        'socio': ''
    }
    success = False
    if request.method == 'POST':
        try:
            idsocio = request.form['idsocio']
            tombo = request.form['tombo']
            retirada = request.form['retirada']

            data['livro'] = livro = db.query_one('select * from livro where tombo = %s' % tombo)
            data['socio'] = socio = db.query_one('select * from socio where id = %s' % idsocio)

            if livro['status'] == 'ESTANTE':
                sql = "insert into emprestimo values(default, '%s', DATE_ADD(CURDATE(), INTERVAL 5 DAY), '%s', '%s')" % (retirada, tombo, idsocio)
                db.insert_bd(sql)
                db.insert_bd('UPDATE livro SET status = "EMPRESTADO" WHERE tombo = "%s" ' % tombo)
                success = True

            elif livro['status'] == 'EMPRESTADO':
                data['error'] = 'Este livro não pode ser emprestado! ' \
                    'Pois já está emprestado.'

            elif livro['status'] == 'PERDIDO':
                data['error'] = 'Este livro não pode ser emprestado! ' \
                    'Pois está perdido.'
                    
            elif livro['status'] == 'EXTRAVIADO':
                data['error'] = 'Este livro não pode ser emprestado! ' \
                    'Pois está extraviado.'

            elif livro['status'] == 'RESERVADO':
                reserva = db.query_one('select * from reserva where tombo = %s and id_socio = %s' % (tombo, idsocio))
                print(reserva)
                if reserva:
                    db.insert_bd("insert into emprestimo values(default, '%s', DATE_ADD(CURDATE(), INTERVAL 5 DAY), '%s', '%s')" % (retirada, tombo, idsocio))
                    db.insert_bd("delete from reserva where id = %s" % reserva['id'])
                    db.insert_bd('UPDATE livro SET status = "EMPRESTADO" WHERE tombo = "%s" ' % tombo)
                    success = True
                
                data['error'] = 'Este livro não pode ser emprestado! ' \
                    'Pois está reservado.'
        except Exception as e:
            print(e)
            return render_template('404.html')

    return render_template('emprestimo/create.html', data=data, success=success)


@bp.route('/emprestimo/<int:id>/devolucao', methods=('GET',))
@login_required
def update(id):
    """Atualiza uma emprestimo pelo seu respectivo id."""
    emprestimo = get_emprestimo(id)
    try:
        db.insert_bd('UPDATE livro SET status = "ESTANTE" WHERE tombo = "%s" ' % emprestimo['tombo'])
        db.insert_bd('DELETE FROM emprestimo WHERE id = "%s"' % emprestimo['id'])
        return redirect(url_for('emprestimo.index'))
    except Exception as e:
        print(e)
        return render_template('404.html')
        
