import customtkinter as ctk

class TransferPopUp(ctk.CTkToplevel):
    def __init__(self, parent, bankaccount):
        super().__init__(parent)
        
        self.title("Secure Transfer")
        self.geometry("400x450")
        self.resizable(False, False)
        
        self.bankaccount = bankaccount
        
        self.after(10, self._set_modal)
        self._setup_ui()

    def _set_modal(self):
        self.grab_set()
        self.focus()
        self.lift()

    def _setup_ui(self):
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self, 
            text="NEW TRANSFER", 
            font=("Arial", 16, "bold")
        )
        self.title_label.grid(row=0, column=0, pady=(20, 10))

        self.target_account_id_input = ctk.CTkEntry(
            self, 
            placeholder_text="Target account ID", 
            width=280, 
            height=35
        )
        self.target_account_id_input.grid(row=1, column=0, pady=10)

        self.amount_input = ctk.CTkEntry(
            self, 
            placeholder_text="Amount (€)", 
            width=280, 
            height=35
        )
        self.amount_input.grid(row=2, column=0, pady=10)

        self.error_label = ctk.CTkLabel(
            self, 
            text="", 
            text_color="#FF5555",
            font=("Arial", 12)
        )
        self.error_label.grid(row=3, column=0, pady=5)

        self.ok_button = ctk.CTkButton(
            self, 
            text="Confirm", 
            width=280, 
            height=40,
            command=self.call_create_transaction
        )
        self.ok_button.grid(row=4, column=0, pady=(20, 10))

        self.cancel_button = ctk.CTkButton(
            self, 
            text="Cancel", 
            fg_color="transparent", 
            border_width=1, 
            width=280, 
            height=35,
            command=self.destroy
        )
        self.cancel_button.grid(row=5, column=0, pady=10)

    def verify_inputs(self):
        pass

    def call_create_transaction(self):
        pass