class Transaction:
    
    def __init__(self):
        pass
    
    
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


    def read(self):
        self.__id = 1
        self.__account_id = 1
        self.__type = "Withdraw"
        self.__date = "18/03/2026"
        self.__category = "Shopping"
        self.__amount = -1245