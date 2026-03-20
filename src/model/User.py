from src.model.DataBase import Database
from src.model.BankAccount import BankAccount

class User():

    def __init__(self):
        self.__db = Database()
        

    def get_email(self):
        return self.__email


    def get_bank_accounts(self):
        return self.__bank_accounts
    

    #CREATE
    def create(self, is_admin:bool, firstname:str, lastname:str, email:str, password:str):
        # create self instance
        self.__is_admin = is_admin
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = self.__db.hash_password(password)
        # open cursor 
        cursor = self.__db.get_cursor()
        
        sql = """
        INSERT INTO user (firstname, lastname, email, password, is_admin)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql,(self.__firstname, self.__lastname, self.__email, self.__password, self.__is_admin))
        self.__db.connect.commit()
        lastrow = cursor.lastrowid
        
        # close cursor and database
        self.__db.close_c()
        # need to instanciate bank_account with transaction and balance
        self.__bank_accounts = [BankAccount()]
        self.__bank_accounts[0].create()
        self.__db.close_db()
        return lastrow
    

    def login(self, email, password):
        id_user = self.__db.login(password,email)
        if isinstance(id_user,int):
            self.read(id_user)
        else:
            print(id_user)


    def read(self, id:int):
        cursor = self.__db.get_cursor()
        sql = """
        SELECT firstname, lastname, email, is_admin
        FROM user
        WHERE id = %s  
        """
        cursor.execute(sql,(id,))
        result = cursor.fetchone()
        self.__firstname = result[0]
        self.__lastname = result[1]
        self.__email = result[2]
        self.__is_admin = result[3]
        self.__id = id
        self.__instantiate_bank_accounts()
        return [self.__id, self.__firstname, self.__lastname, self.__email, self.__is_admin, self.__bank_accounts] 

### NEED TO BE REFACTORED ###
    def update_firstname(self, new_name :str):
        cursor = self.__db.get_cursor()
        sql = """
        UPDATE user
        SET firstname =%s
        WHERE id = %s
        """
        cursor.execute(sql,(new_name,self.__id))
        self.__db.connect.commit()
        self.__db.close_c()
        self.__db.close_db()  
        return
     

    def update_lastname(self, new_lastname:str, id:int):
        cursor = self.__db.get_cursor()
        sql = """
        UPDATE user
        SET lastname =%s
        WHERE id = %s
        """
        cursor.execute(sql,(new_lastname,id))
        self.__db.connect.commit()
        self.__db.close_c()
        self.__db.close_db()  
        return


    def update_email(self, new_email:str, id):
        cursor = self.__db.get_cursor()
        sql = """
        UPDATE user
        SET email =%s
        WHERE id = %s
        """
        cursor.execute(sql,(new_email,id))
        self.__db.connect.commit()
        self.__db.close_c()
        self.__db.close_db()  
        return
### NEED TO BE REFACTORED END ###
 

    def update_password(self, new_password:str):

        cursor = self.__db.get_cursor()
        # DON'T FORGET TO HASH PASSWORD
        new_password = self.__db.hash_password(new_password)

        sql = """
        UPDATE user
        SET password =%s
        WHERE id = %s
        """
        cursor.execute(sql,(new_password,self.__id))
        self.__db.connect.commit()
        self.__db.close_c()
        self.__db.close_db()  
        return
    

    def delete(self, id):
        #DEL CASCADE !
        cursor = self.__db.get_cursor()
        sql = "DELETE FROM user WHERE id=%s"
        cursor.execute(sql, (id,))
        self.__db.connect.commit()
        delete_row = cursor.rowcount
        self.__db.close_c()

        if delete_row == 0:
            print("ECHEC: Aucun utilisateur trouvé avec cet ID.")  
        
        elif delete_row == 1:
            print("REUSSITE: Utilisateur trouvé avec cet ID.")      
        return delete_row


    def __instantiate_bank_accounts(self):

        self.__bank_accounts = []
        cursor = self.__db.get_cursor()
        sql = """
        SELECT bank_account_id
        FROM user_bank_account
        WHERE user_id = %s  
        """
        cursor.execute(sql,(self.__id,))
        results = cursor.fetchall()

        for result in results:
            bank_account = BankAccount()
            bank_account.read(result[0])
            self.__bank_accounts.append(bank_account)
        return