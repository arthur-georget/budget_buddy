import mysql.connector

class Database():

    def __init__(self):
        self.connect = mysql.connector.connect(
            host = "localhost",
            user = "u_bank_admin",
            password = "password",
            database = "db_bank_test"
        )
        
    def cursor_o(self):
        self.cursor = self.connect.cursor()
        return self.cursor

    def close_c(self):
        self.cursor.close()

    def close_db(self):
        self.connect.close()

    def get_cursor(self):
        return self.cursor_o()