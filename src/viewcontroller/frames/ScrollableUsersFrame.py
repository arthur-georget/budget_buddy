import customtkinter as ctk

class ScrollableUsersFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, label_text="User List")
        
        self._add_user_row("User 1")
        self._add_user_row("User 2")
        self._add_user_row("User 3")

    def _add_user_row(self, username):
        row = ctk.CTkFrame(self)
        row.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkLabel(row, text=username).pack(side="left", padx=10)
        ctk.CTkButton(row, text="Select", width=80).pack(side="right", padx=10)