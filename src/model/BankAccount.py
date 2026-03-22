from src.model.DataBase import Database
from src.model.Transaction import Transaction

class BankAccount:

    def __init__(self):
        self.__db = Database()


    def get_id(self):
        return self.__id
    

    def get_balance(self):
        return self.__balance
    

    def get_transactions(self):
        return self.__transactions


    def create(self, balance = 0):
        
        self.__balance = balance
        self.__transactions = []

        cursor = self.__db.get_cursor()
        sql = """ INSERT INTO bank_account (balance)
        VALUES (%s)
        """
        cursor.execute(sql,(balance,))
        self.__db.connect.commit()
        lastrow = cursor.lastrowid
        cursor.close()
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
        cursor.close()

        self.__instantiate_transactions()



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

        cursor.close()



    def update(self):
        pass


    def delete(self):
        pass


    def __instantiate_transactions(self):

        self.__transactions = []
        cursor = self.__db.get_cursor()
        sql = """
        SELECT id
        FROM transaction
        WHERE account_id = %s  
        """
        cursor.execute(sql,(self.__id,))
        results = cursor.fetchall()

        for result in results:
            transaction = Transaction()
            transaction.read(result[0])
            self.__transactions.append(transaction)

        cursor.close()