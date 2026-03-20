#from src.model.User import User
import mysql.connector
import bcrypt

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
    
    def hash_password(self,password):
        hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hash_pw
    
    def __find_hashe_pw(self,email):
        cursor = self.get_cursor()
        sql = """
        SELECT password 
        FROM user
        WHERE email=%s  
        """
        cursor.execute(sql,(email,))
        result = cursor.fetchone()
        self.close_c()
        return result[0]
    
    def verify_bcript_pw(self,password,email):
        hash_stock = self.__find_hashe_pw(email)
        verify_pw = bcrypt.checkpw(password.encode(),hash_stock.encode())
        return verify_pw, hash_stock
        
    def login(self, password, email):
        hashes = self.verify_bcript_pw(password,email)
        cursor = self.get_cursor()
        if hashes[0] == True:
            sql = """
            SELECT id 
            FROM user
            WHERE password =%s AND email=%s  
            """
            cursor.execute(sql,(hashes[1], email))
            result_select = cursor.fetchone()
            self.close_c()
            instance_user = result_select[0]
            self.close_db()
            return instance_user
        else:
            return "Sorry, your email or password is incorrect."