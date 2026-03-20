#from src.model.User import User
import mysql.connector
#import hashlib
#import bcrypt
class Database():

    def __init__(self):
        self.connect = mysql.connector.connect(
            host = "localhost",
            user = "u_bank_admin",
            password = "password",
            database = "db_bank"
        )
        
    def __cursor_o(self):
        self.cursor = self.connect.cursor()
        return self.cursor

    def close_c(self):
        self.cursor.close()

    def close_db(self):
        self.connect.close()

    def get_cursor(self):
        return self.__cursor_o()
    
    #def check_login_password(self, email,password):
    #    #IN PROGRESS
    #    cursor = self.get_cursor()
    #    hashlib.sha
    #    h_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    #    sql = """
    #    SELECT id 
    #    FROM user
    #    WHERE email=%s  
    #    """



    #def login(self, password, email):
    #    #IN PROGRESS
    #    # verify_password method
    #    # verify login password
    #    cursor = self.get_cursor()
    #    sql = """
    #    SELECT id 
    #    FROM user
    #    WHERE password =%s AND email=%s  
    #    """
    #    cursor.execute(sql,(password, email))
    #    result_select = cursor.fetchone()
    #    self.close_c()
    #    instance_user = User()
    #    instance_user.read(result_select[0])
    #    self.close_db()
    #    return instance_user