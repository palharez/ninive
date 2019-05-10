from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required

bp = Blueprint('reserva', __name__)


def get_autor(id):
    try:
        autor = db.query_one('select * from autor where id = %d' % id)

        if autor is None:
            return render_template('404.html')

        return autor
    except:
        return render_template('404.html')

@bp.route('/reserva', methods=('GET',))
@login_required
def index():
    """Exibe todos as emprstimos cadastradas."""
    try:
        reservas = db.query_bd('select * from reserva \
            inner join livro on reserva.tombo = livro.tombo \
            inner join socio on reserva.id_socio = socio.id;')
        return render_template('reserva/index.html', reservas=reservas)
    except Exception as e:
        print(e)
        return render_template('404.html')


@bp.route('/reserva/create', methods=('GET', 'POST'))
@login_required
def reservar():
    """
    Reserva um livro.
    
    Verificar se o livro já não foi reservado.
    """
    data = {
        'error': '',
        'livro': '',
        'socio': ''
    }
    if request.method == 'POST':
        try:
            idsocio = request.form['idsocio']
            tombo = request.form['tombo']

            data['livro'] = livro = db.query_one('select * from livro where tombo = %s' % tombo)
            data['socio'] = socio = db.query_one('select * from socio where id = %s' % idsocio)

            if livro['status'] == 'ESTANTE':
                reservar_livro(tombo, idsocio)
                return redirect(url_for('livro.index'))

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
                    reservar_livro(tombo, idsocio)
                    return redirect(url_for('livro.index'))

        except Exception as e:
            print(e)
            return render_template('404.html')

    return render_template('livro/reserva.html', data=data)
