import os, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from sgb.database import Database


def create_db():
    return Database('tcc_tests')


def truncate(table):
    db = create_db()
    db.insert_bd("delete from %s" % table)
    zero_table(table)

def zero_table(table):
    db = create_db()
    db.insert_bd("ALTER TABLE %s AUTO_INCREMENT = 1" % table)    

def insert(sql):
    db = create_db()
    db.insert_bd(sql)
