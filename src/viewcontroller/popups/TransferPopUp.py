import customtkinter as ctk

class TransferPopUp(ctk.CTkToplevel):
    def __init__(self, parent, bank_account):
        super().__init__(parent)
        self.title("Transfert Sécurisé")
        self.geometry("400x400")
        self.resizable(False, False)
        self.bank_account = bank_account
        self.after(10, self._set_modal)

    def _set_modal(self):
        self.grab_set()
        self.focus()
        self.lift()