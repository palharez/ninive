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


@bp.route('/emprestimo', defaults={'page': 1}, methods=('GET', 'POST'))
@bp.route('/emprestimo/page/<int:page>')
@login_required
def index(page):
    """Exibe todos as emprstimos cadastradas."""
    try:
        perpage = 12
        startat = ( page - 1 ) * perpage
        perpage *= page
        totalemprestimo = db.query_bd('select * from emprestimo \
            inner join livro on emprestimo.tombo = livro.tombo \
            inner join socio on emprestimo.id_socio = socio.id;')
        totalpages = int(len(totalemprestimo) / 12) + 1 
        if request.method == 'POST':
            busca = request.form['busca']
            tipo = request.form['tipo']
            if tipo == "titulo":
                sql = "SELECT emprestimo.*,  \
                    (SELECT s.nome FROM socio s WHERE s.id = emprestimo.id_socio) as 'nome', \
                    (SELECT l.titulo FROM livro l WHERE l.tombo = emprestimo.tombo) as 'titulo' \
                    FROM emprestimo \
                    WHERE (SELECT l.titulo FROM livro l WHERE l.tombo = emprestimo.tombo) \
                    LIKE '%{}%' limit {}, {};".format(busca, startat, perpage)
            elif tipo == "nome":
                sql = "SELECT emprestimo.*,  \
                    (SELECT s.nome FROM socio s WHERE s.id = emprestimo.id_socio) as 'nome', \
                    (SELECT l.titulo FROM livro l WHERE l.tombo = emprestimo.tombo) as 'titulo' \
                    FROM emprestimo \
                    WHERE (SELECT s.nome FROM socio s WHERE s.id = emprestimo.id_socio) \
                    LIKE '%{}%' limit {}, {};".format(busca, startat, perpage)
            elif tipo == "id":
                sql = "SELECT emprestimo.*,  \
                    (SELECT s.nome FROM socio s WHERE s.id = emprestimo.id_socio) as 'nome', \
                    (SELECT l.titulo FROM livro l WHERE l.tombo = emprestimo.tombo) as 'titulo' \
                    FROM emprestimo \
                    WHERE emprestimo.id \
                    LIKE '%{}%' limit {}, {};".format(busca, startat, perpage)
            emprestimos = db.query_bd(sql)
            totalpages = int(len(emprestimos) / 12) + 1 
        else:
            emprestimos = db.query_bd('select * from emprestimo \
            inner join livro on emprestimo.tombo = livro.tombo \
            inner join socio on emprestimo.id_socio = socio.id limit %s, %s;' % (startat, perpage))
        emprestimos = emprestimos[:12]
        return render_template('emprestimo/index.html', emprestimos=emprestimos, page=page, totalpages=totalpages)
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

    return render_template('emprestimo/create.html', data=data, success=success, socios_id=socios_id, livros_tombo=livros_tombo)


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
        

@bp.route('/emprestimo/relatorio', methods=('GET', 'POST'))
@login_required
def relatorio():
    emprestimos = ''
    try:
        editoras = db.query_bd('select * from editora')
        autores = db.query_bd('select * from autor')
        if request.method == 'POST':
            data = request.form['data'].split('/')
            sql = 'select * from emprestimo_morto  \
                    inner join livro on livro.tombo = emprestimo_morto.tombo \
                    inner join socio on socio.id = emprestimo_morto.id_socio \
                    inner join editora on livro.id_editora = editora.id \
                    inner join autor on livro.id_autor = autor.id \
                    where month(emprestimo_morto.retirada) = %d \
                    and year(emprestimo_morto.retirada) = %d;' % (int(data[0]), int(data[1]))
            emprestimos = db.query_bd(sql)
            lengt = len(emprestimos)
            return render_template('emprestimo/relatorio.html', emprestimos=emprestimos, lengt=lengt)
    except Exception as e:
        print(e)
        return render_template('404.html')
    
    return render_template('emprestimo/relatorio.html', emprestimos=emprestimos)