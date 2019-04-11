import pymysql


class Database:

    def __init__(self, dbname):
        self.dbname = dbname

    def create_connction(self):
        host = 'localhost'
        user = 'root'
        password = 'root'
        dbname = self.dbname
        self.con = pymysql.connect(
            host=host, user=user, password=password, db=dbname, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def query_bd(self, sql):
        self.create_connction()
        try:
            self.cur.execute(sql)
            self.con.close()
            return self.cur.fetchall()
        except:
            raise Exception("A query {'query': %s} não funcionou!" % sql)

    def insert_bd(self, sql):
        self.create_connction()
        try:
            self.cur.execute(sql)
            self.con.commit()
            self.con.close()
        except:
            raise Exception("O insert {'insert': %s} não funcionou!" % sql)

    def query_one(self, sql):
        self.create_connction()
        try:
            self.cur.execute(sql)
            return self.cur.fetchone()
            self.con.close()
        except:
            raise Exception("A query {'query': %s} não funcionou!" % sql)