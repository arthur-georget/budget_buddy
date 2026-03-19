import customtkinter as ctk
from src.model.Transaction import Transaction

class ScrollableTransactionsRecordFrame(ctk.CTkScrollableFrame):
    
    def __init__(self, parent, transactions: list[Transaction], **kwargs):
        
        ctk.CTkScrollableFrame.__init__(self, master = parent, **kwargs)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(2, weight=5)
        self.columnconfigure(3, weight=2)
        self.columnconfigure(4, weight=2)

        for i,transaction in enumerate(transactions):
            id = ctk.CTkLabel(self, text=transaction.get_id(), font=("Arial", 12, "bold"))
            id.grid(row=i, column=0, sticky="W", ipadx=10, ipady=5)
            category = ctk.CTkLabel(self, text=transaction.get_category(), font=("Arial", 12, "bold"))
            category.grid(row=i, column=1, sticky="W", ipadx=10, ipady=5)
            date = ctk.CTkLabel(self, text=transaction.get_date(), font=("Arial", 12, "bold"))
            date.grid(row=i, column=2, sticky="W", ipadx=10, ipady=5)
            transaction_type = ctk.CTkLabel(self, text=transaction.get_type(), font=("Arial", 12, "bold"))
            transaction_type.grid(row=i, column=3, sticky="W", ipadx=10, ipady=5)
            amount = ctk.CTkLabel(self, text=transaction.get_amount(), font=("Arial", 12, "bold"))
            amount.grid(row=i, column=4, sticky="W", ipadx=10, ipady=5)