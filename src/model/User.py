from src.model.DataBase import Database
from src.model.BankAccount import BankAccount

class User():

    def __init__(self):
        self.__db = Database()
        self.__id = None
        self.__firstname = None
        self.__lastname = None
        self.__email = None
        self.__is_admin = None
        self.__bank_accounts = []

    # GETTERS
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

        cursor = self.__db.get_cursor()
        
        sql = """
        INSERT INTO user (firstname, lastname, email, password, is_admin)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql,(
            self.__firstname, 
            self.__lastname, 
            self.__email, 
            self.__password, 
            self.__is_admin))
        
        self.__db.connect.commit()
        self.__id = cursor.lastrowid
        cursor.close
        # OLD
        #self.__bank_accounts = [BankAccount()]
        #self.__bank_accounts[0].create()
        #self.__db.close_db()
        
        # NEW
        account = BankAccount()
        account.create()
        self.__bank_accounts =[account]
        return self.__id
    

    def login(self, email, password):
        id_user = self.__db.login(password,email)
        if isinstance(id_user,int):
            self.read(id_user)
        else:
            print(id_user)

    # READ
    def read(self, id:int):
        cursor = self.__db.get_cursor()
        sql = """
        SELECT firstname, lastname, email, is_admin
        FROM user
        WHERE id = %s  
        """
        cursor.execute(sql,(id,))
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            return None
        
        self.__id = id
        self.__firstname = result[0]
        self.__lastname = result[1]
        self.__email = result[2]
        self.__is_admin = result[3]
        self.__instantiate_bank_accounts()
        return [self.__id,
                self.__firstname,
                self.__lastname,
                self.__email,
                self.__is_admin,
                self.__bank_accounts] 

    # UPDATE CONTROLLER
    def __update_field(self, field: str, value):
        cursor = self.__db.get_cursor()

        sql = f"UPDATE user SET {field} = %s WHERE id = %s"
        cursor.execute(sql, (value, self.__id))
        self.__db.connect.commit()
        cursor.close()
    # UPDATERS
    def update_firstname(self, new_name: str):
        self.__update_field("firstname", new_name)
        self.__firstname = new_name

    def update_lastname(self, new_lastname: str):
        self.__update_field("lastname", new_lastname)
        self.__lastname = new_lastname

    def update_email(self, new_email: str):
        self.__update_field("email", new_email)
        self.__email = new_email

    def update_password(self, new_password: str):
        hashed = self.__db.hash_password(new_password)
        self.__update_field("password", hashed)

    def delete(self, id):
        #DEL CASCADE !
        cursor = self.__db.get_cursor()
        sql = "DELETE FROM user WHERE id=%s"
        cursor.execute(sql, (id,))
        self.__db.connect.commit()
        deleted = cursor.rowcount
        cursor.close()

        if deleted == 0:
            print("FAIL: No users were found with this ID.")  
        
        elif deleted == 1:
            print("SUCCESS: User found with this ID.")      
        return deleted


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
        cursor.close()
        for result in results:
            bank_account = BankAccount()
            bank_account.read(result[0])
            self.__bank_accounts.append(bank_account)
        return