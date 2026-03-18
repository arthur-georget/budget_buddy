import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class NewUserFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        label = ctk.CTkLabel(self, text="New User", font=("Arial", 12, "bold"))
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10) 

        self.firstname_input = ctk.CTkEntry(self, placeholder_text="Firstname", width=200)
        self.firstname_input.grid(row=1, column=0, columnspan=2, pady=5)

        self.lastname_input = ctk.CTkEntry(self, placeholder_text="Lastname", width=200)
        self.lastname_input.grid(row=2, column=0, columnspan=2, pady=5)

        self.email_input = ctk.CTkEntry(self, placeholder_text="Email", width=200)
        self.email_input.grid(row=3, column=0, columnspan=2, pady=5)

        self.password_input = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=200)
        self.password_input.grid(row=4, column=0, columnspan=2, pady=5)

        self.password_check_input = ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*", width=200)
        self.password_check_input.grid(row=5, column=0, columnspan=2, pady=5)

        self.create_button = ctk.CTkButton(self, text="Create Account", command=self.call_create_user)
        self.create_button.grid(row=6, column=0, padx=10, pady=20)

        self.cancel_button = ctk.CTkButton(self, text="Cancel", fg_color="gray", 
                                          command=lambda: controller.show_frame("UserConnectionFrame"))
        self.cancel_button.grid(row=6, column=1, padx=10, pady=20)

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