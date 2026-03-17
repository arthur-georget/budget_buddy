import customtkinter as ctk
from functools import partial

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        ctk.CTkFrame.__init__(self, parent)
        
        label = ctk.CTkLabel(self, text ="Main menu", font = ("Arial", 12, "bold"))
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
 
        transactions_record_button = ctk.CTkButton(self, text ="Transactions record",
        command = lambda : controller.show_frame("TransactionsRecordFrame"))
        transactions_record_button.grid(row = 1, column = 1, padx = 10, pady = 10)

        withdraw_button = ctk.CTkButton(self, text ="Withdraw",
        command = partial(self.__ask_amount,"withdraw"))
        withdraw_button.grid(row = 2, column = 1, padx = 10, pady = 10)

        deposit_button = ctk.CTkButton(self, text ="Deposit",
        command = partial(self.__ask_amount,"deposit"))
        deposit_button.grid(row = 3, column = 1, padx = 10, pady = 10)


    def __ask_amount(self, operation_type : str):
        dialog = ctk.CTkInputDialog(text=f"How much money do you want to {operation_type}?", title=f"{operation_type}")
        try:
            amount = float(dialog.get_input())
            if amount < 0:
                print("The amount provided must be > 0.")
                self.__ask_amount(operation_type)
            else:    
                print(amount)
        except:
            print("The amount provided must be a number.")
            self.__ask_amount(operation_type)