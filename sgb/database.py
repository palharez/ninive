import pymysql


class Database:

    def __init__(self):
        host = 'localhost'
        user = 'root'
        password = 'root'
        dbname = 'TCC'
        self.con = pymysql.connect(
            host=host, user=user, password=password, db=dbname, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def query_bd(self, sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except:
            raise Exception("A query {'query': %s} não funcionou!" % sql)

    def insert_bd(self, sql):
        try:
            self.cur.execute(sql)
            self.con.commit()
        except:
            raise Exception("O insert {'insert': %s} não funcionou!" % sql)

    def query_one(self, sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchone()
        except:
            raise Exception("A query {'query': %s} não funcionou!" % sql)