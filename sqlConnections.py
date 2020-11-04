import pymysql
from decouple import config

class dataConnection:
    def __init__(self): 
        host = "192.168.1.51"
        port = 3306
        user = config('SQLUSER')
        password = config('SQLPASS')
        database = config('SQLDATA')

        #this starts the connection to  
        self.conn = pymysql.connect(host = host, port = port, user = user, password = password, database =database)
        self.cursor = self.conn.cursor()


    def get_hash(self, code, purpose):
        sql = """SELECT `hash` FROM mail_token WHERE `code` = %s AND  `purpose` = %s"""

        self.conn.ping(reconnect=True)
        self.cursor.execute(sql, (code, purpose))
        data = self.cursor.fetchall()
        if data:
            return data[0][0]
        else:
            return None

    def verify_user(self, code):
        sql = """UPDATE users SET `verified` = 1 WHERE `code` = %s"""

        try:
            self.conn.ping(reconnect=True)
            self.cursor.execute(sql, code)
            self.conn.commit()
        except  Exception as exc:
            self.conn.rollback()
            print(str(exc))
        
    def get_date(self, code):
        sql = """SELECT `birthday` FROM users WHERE `code` = %s"""

        self.conn.ping(reconnect=True)
        self.cursor.execute(sql, code)
        data = self.cursor.fetchall()

        if data:
            data = data[0][0]
        return data

    def add_homework(self, code, hid, issue_date, due_date, ticked):
        sql = """INSERT INTO homework (`code`, `id`, `issue_date`, `due_date`, `ticked`) VALUES ( %s, %s, %s, %s, %s)"""

        try:
            self.conn.ping(reconnect=True)
            self.cursor.execute(sql, (code, hid, issue_date, due_date, ticked))
            self.conn.commit()
        except  Exception as exc:
            self.conn.rollback()
            print(str(exc))
    
    def mail_get_request(self, userCode, purpose):
        sql = """SELECT `code`, `purpose` FROM mail_token WHERE `code` = %s AND `purpose` = %s"""

        self.conn.ping(reconnect=True)
        self.cursor.execute(sql, (userCode, purpose))

        data = self.cursor.fetchall()
        if data:
            data = data[0]
        return data

    def mail_remove_request(self, userCode, purpose):
        sql = """DELETE FROM mail_token WHERE `code` = %s AND `purpose` = %s"""

        try:
            self.conn.ping(reconnect=True)
            self.cursor.execute(sql, (userCode, purpose))
            self.conn.commit()
        except  Exception as exc:
            self.conn.rollback()
            print(str(exc))

    def mail_add_request(self, userCode, purpose, newhash, date):
        sql="""INSERT INTO mail_token (`code`, `hash`, `purpose`, `time`) VALUES (%s,%s,%s,%s)"""

        try:
            self.conn.ping(reconnect=True)
            self.cursor.execute(sql, (userCode, newhash, purpose, date))
            self.conn.commit()
        except  Exception as exc:
            self.conn.rollback()
            print(str(exc))