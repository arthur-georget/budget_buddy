import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class NewUserFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(8, weight=1)

        label = ctk.CTkLabel(self, text="New User", font=("Arial", 24, "bold"))
        label.grid(row=1, column=0, pady=(0, 20)) 

        self.firstname_input = ctk.CTkEntry(self, placeholder_text="Firstname", width=280, height=35)
        self.firstname_input.grid(row=2, column=0, pady=5)

        self.lastname_input = ctk.CTkEntry(self, placeholder_text="Lastname", width=280, height=35)
        self.lastname_input.grid(row=3, column=0, pady=5)

        self.email_input = ctk.CTkEntry(self, placeholder_text="Email", width=280, height=35)
        self.email_input.grid(row=4, column=0, pady=5)

        self.password_input = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=280, height=35)
        self.password_input.grid(row=5, column=0, pady=5)

        self.password_check_input = ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*", width=280, height=35)
        self.password_check_input.grid(row=6, column=0, pady=5)

        self.create_button = ctk.CTkButton(self, text="Create Account", width=280, height=40, command=self.call_create_user)
        self.create_button.grid(row=7, column=0, pady=(20, 10))

        self.cancel_button = ctk.CTkButton(self, text="Cancel", fg_color="gray", width=280, height=35,
                                          command=lambda: controller.show_frame("UserConnectionFrame"))
        self.cancel_button.grid(row=8, column=0, pady=(0, 10), sticky="n")

    def verify_inputs(self):
        if not all([self.firstname_input.get(), self.email_input.get(), self.password_input.get()]):
            return False
        return self.password_input.get() == self.password_check_input.get()

    def instantiate_wrong_input_popup(self):
        CTkMessagebox(title="Error", message="Invalid inputs or passwords mismatch", icon="cancel")

    def call_create_user(self):
        if self.verify_inputs():
            CTkMessagebox(title="Success", message="User created successfully", icon="check")
            self.controller.show_frame("UserConnectionFrame")
        else:
            self.instantiate_wrong_input_popup()