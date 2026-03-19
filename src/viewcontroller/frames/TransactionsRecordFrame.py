import customtkinter as ctk
from src.model.Transaction import Transaction
from src.viewcontroller.frames.ScrollableTransactionsRecordFrame import ScrollableTransactionsRecordFrame

class TransactionsRecordFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, user): 
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.user = user
        
        label = ctk.CTkLabel(self, text="Transactions Record", font=("Arial", 12, "bold"))
        label.grid(row=0, column=1, padx=10, pady=10) 
 
        main_button = ctk.CTkButton(self, text="Main menu",
                                    command=lambda: controller.show_frame("MainFrame"))
        main_button.grid(row=1, column=1, padx=10, pady=10)

        transactions = []
        for i in range(20):
            transaction = Transaction()
            transaction.read()
            transactions.append(transaction)

        scrollable_transactions = ScrollableTransactionsRecordFrame(self, transactions, width=500)
        scrollable_transactions.grid(row=1, column=3, padx=10, pady=10)