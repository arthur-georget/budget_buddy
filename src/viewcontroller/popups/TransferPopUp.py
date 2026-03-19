import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class TransferPopUp(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title("Secure Transfer")
        self.geometry("400x480")
        self.resizable(False, False)
        self.account = parent.get_selected_account()
        
        self.grid_columnconfigure(0, weight=1)
        self.after(10, self._set_modal)
        self._setup_ui()

    def _set_modal(self):
        self.grab_set()
        self.focus_force()

    def _setup_ui(self):
        ctk.CTkLabel(self, text="NEW TRANSFER", font=("Arial", 20, "bold")).grid(row=0, pady=(30, 20))

        self.target_input = ctk.CTkEntry(self, placeholder_text="Target account ID", width=300, height=40)
        self.target_input.grid(row=1, pady=10)

        self.amount_input = ctk.CTkEntry(self, placeholder_text="Amount (€)", width=300, height=40)
        self.amount_input.grid(row=2, pady=10)

        self.error_label = ctk.CTkLabel(self, text="", text_color="#FF5555", font=("Arial", 12))
        self.error_label.grid(row=3, pady=5)

        ctk.CTkButton(self, text="Confirm Transfer", width=300, height=45, 
                      command=self.call_create_transaction).grid(row=4, pady=(20, 10))

        ctk.CTkButton(self, text="Cancel", fg_color="transparent", border_width=1, 
                      width=300, height=40, command=self.destroy).grid(row=5, pady=10)

    def verify_inputs(self):
        target = self.target_input.get().strip()
        amount_s = self.amount_input.get().strip()

        if not target or not amount_s:
            return False, "All fields are required."
        
        try:
            amount = float(amount_s)
            if amount <= 0: return False, "Amount must be positive."
            if hasattr(self.account, 'balance') and amount > self.account.balance:
                return False, "Insufficient funds."
        except ValueError:
            return False, "Please enter a valid number."

        return True, None

    def call_create_transaction(self):
        is_valid, msg = self.verify_inputs()
        if not is_valid:
            self.error_label.configure(text=msg)
            return

        msg_box = CTkMessagebox(title="Success", message="Transfer successful!", icon="check")
        if msg_box.get() == "OK":
            self.destroy()