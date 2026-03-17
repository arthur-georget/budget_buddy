import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        ctk.CTkFrame.__init__(self, parent)
        
        label = ctk.CTkLabel(self, text ="Main menu", font = ("Arial", 12, "bold"))
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
 
        transactions_record_button = ctk.CTkButton(self, text ="Transactions record",
        command = lambda : controller.show_frame("transactions_recordFrame"))
        transactions_record_button.grid(row = 1, column = 1, padx = 10, pady = 10)

        withdraw_button = ctk.CTkButton(self, text ="Withdraw",
        command = self.__ask_withdraw_amount)
        withdraw_button.grid(row = 2, column = 1, padx = 10, pady = 10)

        deposit_button = ctk.CTkButton(self, text ="Deposit",
        command = self.__ask_deposit_amount)
        deposit_button.grid(row = 3, column = 1, padx = 10, pady = 10)


    def __ask_withdraw_amount(self):
        print("Withdraw")
        pass

    
    def __ask_deposit_amount(self):
        print("Deposit")
        pass
