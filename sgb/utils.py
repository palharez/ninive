import os
from werkzeug import secure_filename

import sys
from sgb import db
import datetime
from datetime import timedelta

root = os.path.dirname((os.path.abspath(__file__)))
root += '/static/images'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def upload_file(file):
    if file.filename == '':
        raise Exception('Arquivo sem nome!')

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(root, filename))

    return file


def add_punicao(data, id_socio):
    db.insert_bd('insert into punicao values(default, %s, "%s")' % (id_socio, data))
    db.insert_bd('update socio set status = "SUSPENSO" where id = %d' % id_socio)


def atualiza_punicao_socio(id_emprestimo):
    emprestimos = db.query_bd('select * from emprestimo where id = %s' % id_emprestimo)
    data_atual = datetime.date.today()

    for emprestimo in emprestimos:
        data_devolucao = emprestimo['devolucao']

        if data_atual >= data_devolucao + timedelta(days=3) and data_atual < data_devolucao + timedelta(days=29):
            add_punicao(data_atual + timedelta(days=30), emprestimo['id_socio'])
            
        elif data_atual >= data_devolucao + timedelta(days=29) and data_atual < data_devolucao + timedelta(days=60):
            add_punicao(data_atual + timedelta(days=90), emprestimo['id_socio'])

        elif data_atual >= data_devolucao + timedelta(days=60) and data_atual < data_devolucao + timedelta(days=120):
            add_punicao(data_atual + timedelta(days=120), emprestimo['id_socio'])

        elif data_atual >= data_devolucao + timedelta(days=120) and data_atual < data_devolucao + timedelta(days=180):
            add_punicao(data_atual + timedelta(days=210), emprestimo['id_socio'])

        elif data_devolucao >= data_atual + timedelta(days=180):
            add_punicao(data_atual + timedelta(days=365), emprestimo['id_socio'])
        

def atualizao_status_socio():
    punicoes = db.query_bd('select * from punicao')
    for punicao in punicoes:
        data_punicao = punicao['data_punicao']
        if datetime.date.today() > data_punicao:
            db.insert_bd('delete from punicao where id = %d' % punicao['id'])
            db.insert_bd('update socio set status = "ATIVO" where id = %d' % punicao['id_socio'])