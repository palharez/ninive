import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from sgb import db

bp = Blueprint('funcionario', __name__)

@bp.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        matricula = int(request.form['matricula'])

        error = None
        funcionario = db.query_one('select * from funcionario where matricula = %d' % matricula)

        if funcionario is None:
            error = 'Incorrect username.'

        if error is None:
            session.clear()
            session['funcionario_matricula'] = funcionario['matricula']
            return redirect(url_for('autor.index'))

        flash(error)

    return render_template('funcionario/login.html')


@bp.before_app_request
def load_logged_in_user():
    funcionario_matricula = session.get('funcionario_matricula')

    if funcionario_matricula is None:
        g.funcionario = None
    else:
        g.funcionario = db.query_one('select * from funcionario where matricula = %d' % funcionario_matricula)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('funcionario.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.funcionario is None:
            return redirect(url_for('funcionario.login'))

        return view(**kwargs)

    return wrapped_view