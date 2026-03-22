from src.model.DataBase import Database

class Transaction:
    
    def __init__(self):
        self.__db = Database()
    
    
    def get_id(self):
        return self.__id
    

    def get_account_id(self):
        return self.__account_id
    

    def get_type(self):
        return self.__type
    

    def get_date(self):
        return self.__date
    

    def get_category(self):
        return self.__category


    def get_amount(self):
        return self.__amount

    def create(self):
        pass


    def read(self, id: int):

        cursor = self.__db.get_cursor()
        sql = """
        SELECT account_id, type, date, category, amount
        FROM transaction
        WHERE id = %s
        """
        cursor.execute(sql,(id,))
        result = cursor.fetchone()
        self.__id = id
        self.__account_id = result[0]
        self.__type = result[1]
        self.__date = result[2]
        self.__category = result[3]
        self.__amount = result[4]

        cursor.close()
        self.__db.close_db()