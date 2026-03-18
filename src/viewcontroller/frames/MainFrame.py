from src.model.BankAccount import BankAccount

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.viewcontroller.popups.TransferPopUp import TransferPopUp

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        ctk.CTkFrame.__init__(self, parent)

        self.__account_selected = BankAccount()

        label = ctk.CTkLabel(self, text ="Main menu", font = ("Arial", 12, "bold"))
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
 
        transactions_record_button = ctk.CTkButton(self, text ="Transactions record",
        command = lambda : controller.show_frame("TransactionsRecordFrame"))
        transactions_record_button.grid(row = 1, column = 1, padx = 10, pady = 10)

        withdraw_button = ctk.CTkButton(self, text ="Withdraw",
        command = lambda : self.__ask_amount("withdraw"))
        withdraw_button.grid(row = 2, column = 1, padx = 10, pady = 10)

        deposit_button = ctk.CTkButton(self, text ="Deposit",
        command = lambda : self.__ask_amount("deposit"))
        deposit_button.grid(row = 3, column = 1, padx = 10, pady = 10)

        transfer_button = ctk.CTkButton(self, text ="Transfer",
        command = self.__instantiate_transfer_popup)
        transfer_button.grid(row = 4, column = 1, padx = 10, pady = 10)


    def __ask_amount(self, operation_type : str):
        dialog = ctk.CTkInputDialog(text=f"How much money do you want to {operation_type}?", title=f"{operation_type.title()}")
        user_input = dialog.get_input()
        if user_input is not None:
            try:
                amount = float(user_input)
                if amount < 0:
                    warning_message = CTkMessagebox(title="Error: Amount provided is negative", 
                                              message="The amount provided should be positive.", 
                                              icon="warning",
                                              option_1="Cancel",
                                              option_2="Retry")
                    if warning_message.get()=="Retry":
                        self.__ask_amount(operation_type)
                else:
                    try:
                        # REPLACE THIS COMMENT WITH User.BankAccount.new_transaction()
                        # AND User.BankAccount.update(new_balance)
                        CTkMessagebox(title=f"{operation_type.title()} success.",
                                                           message=f"{amount}€ {operation_type} done successfully.",
                                                           icon="check")
                    except:
                        error_message = CTkMessagebox(title=f"{operation_type.title()} error",
                                                      message=f"Something went wrong during {operation_type}.",
                                                      icon="cancel",
                                                      option_1="Cancel",
                                                      option_2="Retry")
                        if error_message.get() == "Retry":
                            self.__ask_amount(operation_type)
                    
            except:
                warning_message = CTkMessagebox(title="Error: Amount provided is not a number.", 
                                              message="The amount provided should be a number.", 
                                              icon="warning",
                                              option_1="Cancel",
                                              option_2="Retry")
                if warning_message.get()=="Retry":
                    self.__ask_amount(operation_type)

    def __instantiate_transfer_popup(self):
        TransferPopUp(self, self.__account_selected)