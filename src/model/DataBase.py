import mysql.connector
import bcrypt

class Database():
    def __init__(self):
        self.connect = None
        self.__connect_db()
    
    def __connect_db(self):
        self.connect = mysql.connector.connect(
            host = "localhost",
            user = "u_bank_admin",
            password = "password",
            database = "db_bank")
        
    def get_cursor(self):
        self.__connect_db()
        return self.connect.cursor()

    def close_db(self):
        if self.connect and self.connect.is_connected():
            self.connect.close()
    
    def hash_password(self,password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def __verify_bcript_pw(self,password,email):
        cursor = self.get_cursor()
        sql = """
        SELECT password 
        FROM user
        WHERE email=%s  
        """
        cursor.execute(sql,(email,))
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            return False, None
        else:
            stored_hash = result[0]
            ok = bcrypt.checkpw(password.encode(), stored_hash.encode())
            return ok, stored_hash
      
    def login(self, password, email):
        ok, stored_hash = self.__verify_bcript_pw(password, email)
        if ok == False:
            return "Sorry, your email or password is incorrect."
        else:
            cursor = self.get_cursor()
            sql ="""SELECT id
                           FROM user
                           WHERE email = %s AND password =%s"""
            cursor.execute(sql, (email, stored_hash))
            result = cursor.fetchone()
            cursor.close()
            return result[0]