import customtkinter as ctk
import datetime
from src.model.User import User
from src.model.Transaction import Transaction
from src.viewcontroller.frames.ScrollableTransactionsRecordFrame import ScrollableTransactionsRecordFrame
from src.viewcontroller.frames.ScrollableFilterFrame import ScrollableFilterFrame


class TransactionsRecordFrame(ctk.CTkFrame):


    def __init__(self, parent, controller, user): 

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        label = ctk.CTkLabel(self, text="Transactions Record", font=("Arial", 12, "bold"))
        label.grid(row=0, column=1, padx=10, pady=10) 
 
        main_button = ctk.CTkButton(self, text ="Main menu",
        command = lambda : controller.show_frame("MainFrame"))
        main_button.grid(row = 1, column = 1, padx = 10, pady = 10)




    def set_user(self, user: User):

        self.__user = user
        self.__init_frame_content()
        print(f"TransactionsRecordFrame: {self.__user.get_email()}")


    def __init_frame_content(self):

        self.__transactions = self.__user.get_bank_accounts()[self.__user.selected_bank_account_index].get_transactions()
        self.__build_filters()
        self.__build_transactions_frame()


    def __build_filters(self):

        categories = []
        transaction_types = []
        dates = []

        for transaction in self.__transactions:

            category = transaction.get_category()
            if category not in categories:
                categories.append(category)

            transaction_type = transaction.get_type()
            if transaction_type not in transaction_types:
                transaction_types.append(transaction_type)

            date = transaction.get_date()
            if date not in dates:
                dates.append(date)

        self.__scrollable_category_filter = ScrollableFilterFrame(self, categories, "Filter by category", radio=True, width=100, height=35)
        self.__scrollable_category_filter.grid(row = 1, column = 3, padx = 10, pady = 10)

        self.__scrollable_transaction_type_filter = ScrollableFilterFrame(self, transaction_types, "Filter by type", radio=True, width=100, height=35)
        self.__scrollable_transaction_type_filter.grid(row = 1, column = 4, padx = 10, pady = 10)

        self.__scrollable_start_date_filter = ScrollableFilterFrame(self, dates, "Choose start date", radio=True, width=100, height=35)
        self.__scrollable_start_date_filter.grid(row = 1, column = 5, padx = 10, pady = 10)

        self.__scrollable_end_date_filter = ScrollableFilterFrame(self, dates, "Choose end date", radio=True, width=100, height=35)
        self.__scrollable_end_date_filter.grid(row = 1, column = 6, padx = 10, pady = 10)

        filter_by_date_range_button = ctk.CTkButton(self, text ="Apply filters",
        command = self.__filter_transactions)
        filter_by_date_range_button.grid(row = 1, column = 7, padx = 10, pady = 10)


    def __build_transactions_frame(self):

        category_filter = self.__scrollable_category_filter.get_selected_filter()
        transaction_type_filter = self.__scrollable_transaction_type_filter.get_selected_filter()
        start_date_filter = self.__str_to_datetime(self.__scrollable_start_date_filter.get_selected_filter())
        end_date_filter = self.__str_to_datetime(self.__scrollable_end_date_filter.get_selected_filter())
        
        transactions = []

        for transaction in self.__transactions:
            transactions.append(transaction)

        for i in range(len(transactions)-1,0,-1):
            if ((category_filter != "" and transactions[i].get_category() != category_filter) or
                (transaction_type_filter != "" and transactions[i].get_type() != transaction_type_filter) or
                (start_date_filter != "" and (transactions[i].get_date() < start_date_filter)) or
                (end_date_filter != "" and  (transactions[i].get_date() > end_date_filter))):
                transactions.pop(i)

        if ((category_filter != "" and transactions[0].get_category() != category_filter) or
                (transaction_type_filter != "" and transactions[0].get_type() != transaction_type_filter) or
                (start_date_filter != "" and (transactions[0].get_date() < start_date_filter)) or
                (end_date_filter != "" and  (transactions[0].get_date() > end_date_filter))):
                transactions.pop(0)
            

        scrollable_transactions = ScrollableTransactionsRecordFrame(self, transactions, height=500, width=730)
        scrollable_transactions.grid(row = 2, column = 3, columnspan = 5, padx = 10, pady = 10)


    def __filter_transactions(self):
        
        print("filter_transactions")
        print(self.__scrollable_category_filter.get_selected_filter())
        print(self.__scrollable_transaction_type_filter.get_selected_filter())
        print(self.__scrollable_start_date_filter.get_selected_filter())
        print(self.__scrollable_end_date_filter.get_selected_filter())
        self.__build_transactions_frame()


    def __str_to_datetime(self, str_to_convert: str):
        if str_to_convert == "":
            return ""
        else:
            format = '%Y-%m-%d %H:%M:%S'
            converted_datetime = datetime.datetime.strptime(str_to_convert, format)
            return converted_datetime