import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class NewUserFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        super().__init__(parent)
        self.controller = controller
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 8), weight=1)

        ctk.CTkLabel(self, text="Create Account", font=("Arial", 28, "bold")).grid(row=1, pady=(0, 25)) 

        self.firstname = ctk.CTkEntry(self, placeholder_text="Firstname", width=320, height=40)
        self.firstname.grid(row=2, pady=7)
        self.lastname = ctk.CTkEntry(self, placeholder_text="Lastname", width=320, height=40)
        self.lastname.grid(row=3, pady=7)
        self.email = ctk.CTkEntry(self, placeholder_text="Email", width=320, height=40)
        self.email.grid(row=4, pady=7)
        self.password = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=320, height=40)
        self.password.grid(row=5, pady=7)
        self.confirm = ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*", width=320, height=40)
        self.confirm.grid(row=6, pady=7)

        ctk.CTkButton(self, text="Sign Up", width=320, height=45, 
                      command=self.call_create_user).grid(row=7, pady=(25, 10))

        ctk.CTkButton(self, text="Back to Login", fg_color="transparent", border_width=1, 
                      width=320, height=35, command=lambda: controller.show_frame("UserConnectionFrame")).grid(row=8, sticky="n")

    def call_create_user(self):
        if not self.email.get() or self.password.get() != self.confirm.get():
            CTkMessagebox(title="Error", message="Invalid inputs or passwords mismatch", icon="cancel")
        else:
            CTkMessagebox(title="Success", message="Account created!", icon="check")
            self.controller.show_frame("UserConnectionFrame")