import customtkinter as ctk
from src.model.Transaction import Transaction
from src.viewcontroller.frames.ScrollableTransactionsRecordFrame import ScrollableTransactionsRecordFrame
from src.viewcontroller.frames.ScrollableFilterFrame import ScrollableFilterFrame

class TransactionsRecordFrame(ctk.CTkFrame):

    def __init__(self, parent, controller): 

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.user = user
        
        label = ctk.CTkLabel(self, text="Transactions Record", font=("Arial", 12, "bold"))
        label.grid(row=0, column=1, padx=10, pady=10) 
 
        main_button = ctk.CTkButton(self, text ="Main menu",
        command = lambda : controller.show_frame("MainFrame"))
        main_button.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        transactions = []
        for i in range(1,101):
            transaction = Transaction()
            transaction.read(i)
            transactions.append(transaction)

        categories = []
        transaction_types = []
        dates = []

        for transaction in transactions:

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

        scrollable_transactions = ScrollableTransactionsRecordFrame(self, transactions, width=500)
        scrollable_transactions.grid(row = 2, column = 3, columnspan = 5, padx = 10, pady = 10)


    def __filter_transactions(self):
        
        print("filter_transactions")
        print(self.__scrollable_category_filter.get_selected_filter())
        print(self.__scrollable_transaction_type_filter.get_selected_filter())
        print(self.__scrollable_start_date_filter.get_selected_filter())
        print(self.__scrollable_end_date_filter.get_selected_filter())