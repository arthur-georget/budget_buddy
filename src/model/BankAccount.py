from src.model.DataBase import Database

class BankAccount:

    def __init__(self):
        self.__db = Database()


    def get_id(self):
        return self.__id
    

    def get_balance(self):
        return self.__balance
    

    def create(self, id_user:int, balance_account = 1):
        cursor = self.__db.get_cursor()
        
        sql = """ INSERT INTO bank_account (id, balance)
        VALUES (%s, %s)
        """
        cursor.execute(sql,(id_user, balance_account))
        self.__db.connect.commit()
        lastrow = cursor.lastrowid
        self.__db.close_c()
        self.__db.close_db()
        return lastrow

    def read(self, id: int):

        cursor = self.__db.get_cursor()
        sql = """
        SELECT balance
        FROM bank_account
        WHERE id = %s
        """
        cursor.execute(sql,(id,))
        result = cursor.fetchone()
        self.__id = id
        self.__balance = result[0]

        self.__db.close_c()
        self.__db.close_db()

    def read_with_transaction(self, id_user):
        cursor = self.__db.get_cursor()
        sql = """
        SELECT balance, transaction
        FROM bank_account
        WHERE id = %s
        """
        cursor.execute(sql,(id_user,))
        result = cursor.fetchone()
        self.__id = id
        self.__balance = result[0]

        self.__db.close_c()
        self.__db.close_db()

    def update(self):
        pass


    def delete(self):
        pass