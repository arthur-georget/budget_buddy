import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class UserConnectionFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1)

        label = ctk.CTkLabel(self, text="User Connection", font=("Arial", 24, "bold"))
        label.grid(row=1, column=0, pady=(0, 30)) 

        self.email_input = ctk.CTkEntry(self, placeholder_text="Email", width=280, height=40)
        self.email_input.grid(row=2, column=0, pady=10)

        self.password_input = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=280, height=40)
        self.password_input.grid(row=3, column=0, pady=10)

        self.login_button = ctk.CTkButton(self, text="Login", width=280, height=45, compound="left", command=self.login)
        self.login_button.grid(row=4, column=0, pady=(20, 10))

        self.create_account_button = ctk.CTkButton(self, text="New Account", width=280, height=40,
                                                  fg_color="transparent", border_width=1,
                                                  command=lambda: controller.show_frame("NewUserFrame"))
        self.create_account_button.grid(row=5, column=0, pady=10)

    def credentials_check(self):
        return self.email_input.get() == "admin" and self.password_input.get() == "1234"

    def instantiate_wrong_credentials_popup(self):
        CTkMessagebox(title="Login Error", message="Wrong email or password.", icon="warning")

    def login(self):
        if self.credentials_check():
            self.controller.show_frame("MainFrame")
        else:
            self.instantiate_wrong_credentials_popup()