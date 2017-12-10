import MySQLdb as my

class MyDB():

    def __init__(self,host,database,username,password):
        self.host = host 
        self.database = database
        self.username = username
        self.password = password 

    def connect_mysql(self):
        connection_result = my.connect(host=self.host,
                                   user=self.username,
                                   passwd=self.password,
                                   db=self.database)
        return connection_result;

class Querys():

    def __init__(self,db):
        self.db = db
        self.cursor = db.cursor()

    def query_fetch_one(self, sql_string):
        self.cursor.execute(sql_string)
        query_result = self.cursor.fetchone()
        self.close_connection()
        return query_result

    def query_fetch_all(self, sql_string):
        self.cursor.execute(sql_string)
        query_result = self.cursor.fetchall()
        return query_result

    def query_commit(self, sql_string):
        self.cursor.execute(sql_string)
        self.db.commit()

    def close_connection(self):
        self.cursor.close()

