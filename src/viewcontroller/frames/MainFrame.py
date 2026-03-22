from src.model.BankAccount import BankAccount
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.model.User import User
from src.viewcontroller.popups.TransferPopUp import TransferPopUp
from src.viewcontroller.frames.ScrollableFilterFrame import ScrollableFilterFrame


class MainFrame(ctk.CTkFrame):

    def __init__(self, parent, controller, user): 
        
        self.__controller = controller

        ctk.CTkFrame.__init__(self, parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        self.app_name = ctk.CTkLabel(self, text="Budget Buddy", font=("Arial", 32, "bold"), text_color="#1f538d")
        self.app_name.grid(row=0, column=0, padx=30, pady=30, sticky="nw")

        self.left_menu = ctk.CTkFrame(self, fg_color="transparent")
        self.left_menu.grid(row=1, column=0, sticky="n", padx=30)

        buttons = [
            ("Transactions record", lambda: self.__controller.show_frame("TransactionsRecordFrame")),
            ("Withdraw", lambda: self.__ask_amount("withdraw")),
            ("Deposit", lambda: self.__ask_amount("deposit")),
            ("Transfer", self.__instantiate_transfer_popup)
        ]

        for text, cmd in buttons:
            btn = ctk.CTkButton(self.left_menu, text=text, command=cmd, width=220, height=45, font=("Arial", 13, "bold"))
            btn.pack(pady=15)


    def get_selected_account(self):

        return self.__selected_bank_account


    def __ask_amount(self, operation_type : str):

        dialog = ctk.CTkInputDialog(text=f"How much money to {operation_type}?", title=operation_type.title())
        user_input = dialog.get_input()
        if user_input:
            try:
                amount = float(user_input)
                if amount > 0:
                    CTkMessagebox(title="Success", message=f"{amount}€ {operation_type} successful.", icon="check")
                else:
                    CTkMessagebox(title="Error", message="Amount must be positive.", icon="warning")
            except ValueError:
                CTkMessagebox(title="Error", message="Please enter a valid number.", icon="cancel")


    def __instantiate_transfer_popup(self):

        TransferPopUp(self)

    
    def set_user(self, user: User):

        self.__user = user
        self.__select_bank_account()
        print(f"MainFrame: {self.__user.get_email()}")


    def filter_action(self, event):

        index = int(self.__scrollable_bank_account_filter.get_selected_filter())
        self.__select_bank_account(index)


    def __select_bank_account(self, index:int = 0):

        self.__selected_bank_account = self.__user.get_bank_accounts()[index]
        self.__balance = self.__selected_bank_account.get_balance()
        self.__update_infos()
        self.__balance_history = [1100.0, 1250.0, 1150.0, 1300.0, 1250.0]


    def __update_infos(self):

        indexes = []
        for i in range(len(self.__user.get_bank_accounts())):
            indexes.append(f"{i}")
        self.__scrollable_bank_account_filter = ScrollableFilterFrame(self, indexes, "Accounts available", height = 60)
        self.__scrollable_bank_account_filter.grid(row= 2, column = 0, pady=20)

        

        self.__dashboard_frame = ctk.CTkFrame(self, fg_color=("#DBEAFE", "#2D2D2D"), corner_radius=20)
        self.__dashboard_frame.grid(row=0, column=1, rowspan=2, padx=30, pady=30, sticky="nsew")

        ctk.CTkLabel(self.__dashboard_frame, text="Balance", font=("Arial", 16, "bold"), text_color=("#1e40af", "#93c5fd")).pack(pady=(40, 5))
        
        self.__balance_label = ctk.CTkLabel(self.__dashboard_frame, text=f"{self.__balance:,.1f} €", font=("Arial", 48, "bold"), text_color=("#1A56DB", "#60a5fa"))
        self.__balance_label.pack(pady=10)

        ctk.CTkLabel(self.__dashboard_frame, text="Monthly expenses", font=("Arial", 14, "bold"), text_color=("#1e40af", "#93c5fd")).pack(pady=(40, 10))
        
        self.__chart_card = ctk.CTkFrame(self.__dashboard_frame, fg_color=("#FFFFFF", "#3D3D3D"), corner_radius=15)
        self.__chart_card.pack(padx=30, pady=20, fill="both", expand=True)
        
        ctk.CTkLabel(self.__chart_card, text="[ Linear chart ]", font=("Arial", 12, "italic"), text_color="gray").place(relx=0.5, rely=0.5, anchor="center")