from src.model.BankAccount import BankAccount
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.viewcontroller.popups.TransferPopUp import TransferPopUp

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.__selected_account = BankAccount()
        self.__selected_account.read(1)
        self.__balance = self.__selected_account.get_balance()
        self.__balance_history = [1100.0, 1250.0, 1150.0, 1300.0, 1250.0]
        

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        self.app_name = ctk.CTkLabel(self, text="Budget Buddy", font=("Arial", 32, "bold"), text_color="#1f538d")
        self.app_name.grid(row=0, column=0, padx=30, pady=30, sticky="nw")

        self.left_menu = ctk.CTkFrame(self, fg_color="transparent")
        self.left_menu.grid(row=1, column=0, sticky="n", padx=30)

        buttons = [
            ("Transactions record", lambda: controller.show_frame("TransactionsRecordFrame")),
            ("Withdraw", lambda: self.__ask_amount("withdraw")),
            ("Deposit", lambda: self.__ask_amount("deposit")),
            ("Transfer", self.__instantiate_transfer_popup)
        ]

        for text, cmd in buttons:
            btn = ctk.CTkButton(self.left_menu, text=text, command=cmd, width=220, height=45, font=("Arial", 13, "bold"))
            btn.pack(pady=15)

        self.dashboard_frame = ctk.CTkFrame(self, fg_color=("#DBEAFE", "#2D2D2D"), corner_radius=20)
        self.dashboard_frame.grid(row=0, column=1, rowspan=2, padx=30, pady=30, sticky="nsew")

        ctk.CTkLabel(self.dashboard_frame, text="Solde Actuel", font=("Arial", 16, "bold"), text_color=("#1e40af", "#93c5fd")).pack(pady=(40, 5))
        
        self.balance_label = ctk.CTkLabel(self.dashboard_frame, text=f"{self.__balance:,.1f} €", font=("Arial", 48, "bold"), text_color=("#1A56DB", "#60a5fa"))
        self.balance_label.pack(pady=10)

        ctk.CTkLabel(self.dashboard_frame, text="Dépenses Mensuelles", font=("Arial", 14, "bold"), text_color=("#1e40af", "#93c5fd")).pack(pady=(40, 10))
        
        self.chart_card = ctk.CTkFrame(self.dashboard_frame, fg_color=("#FFFFFF", "#3D3D3D"), corner_radius=15)
        self.chart_card.pack(padx=30, pady=20, fill="both", expand=True)
        
        ctk.CTkLabel(self.chart_card, text="[ Graphique Linéaire ]", font=("Arial", 12, "italic"), text_color="gray").place(relx=0.5, rely=0.5, anchor="center")

    def get_selected_account(self):
        return self.__selected_account

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