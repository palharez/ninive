import pymysql.cursors

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host='localhost,
                               user='root',
                               password='root',
                               db='tcc',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

    return g.db
