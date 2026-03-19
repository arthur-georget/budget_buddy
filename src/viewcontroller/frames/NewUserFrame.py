import customtkinter as ctk

class NewUserFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, user):
        super().__init__(parent)
        self.controller = controller
        self.user = user

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 5), weight=1)

        ctk.CTkLabel(self, text="Budget Buddy", font=("Arial", 32, "bold"), text_color="#1f538d").grid(row=1, pady=(0, 10))
        
        self.email_input = ctk.CTkEntry(self, placeholder_text="Email", width=300, height=45)
        self.email_input.grid(row=2, pady=10)

        self.password_input = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=300, height=45)
        self.password_input.grid(row=3, pady=10)

        ctk.CTkButton(self, text="Register", width=300, height=50, command=self.register).grid(row=4, pady=20)
        ctk.CTkButton(self, text="Back", fg_color="transparent", border_width=1, 
                      command=lambda: controller.show_frame("UserConnectionFrame")).grid(row=5, sticky="n")

    def register(self):
        self.controller.show_frame("UserConnectionFrame")