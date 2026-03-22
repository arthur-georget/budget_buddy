import customtkinter as ctk
from src.model.User import User
class NewUserFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, user):
        ctk.CTkFrame.__init__(self, parent)

        self.controller = controller
        self.__user = user

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 8), weight=1)

        ctk.CTkLabel(self, text="Budget Buddy", font=("Arial", 32, "bold"), text_color="#1f538d").grid(row=1, pady=(0, 10))
        
        self.firstname_input = ctk.CTkEntry(self, placeholder_text="Firstname", width=300, height=45)
        self.firstname_input.grid(row=2, pady=10)

        self.lastname_input = ctk.CTkEntry(self, placeholder_text="Lastname", width=300, height=45)
        self.lastname_input.grid(row=3, pady=10)
        
        self.email_input = ctk.CTkEntry(self, placeholder_text="Email", width=300, height=45)
        self.email_input.grid(row=4, pady=10)

        self.password_input = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=300, height=45)
        self.password_input.grid(row=5, pady=10)

        self.password_check_input = ctk.CTkEntry(self, placeholder_text="Password Confirmation", show="*", width=300, height=45)
        self.password_check_input.grid(row=6, pady=10)
        
        ctk.CTkButton(self, text="Register", width=300, height=50, command=self.register).grid(row=7, pady=20)
        ctk.CTkButton(self, text="Back", fg_color="transparent", border_width=1, 
                      command=lambda: controller.show_frame("UserConnectionFrame")).grid(row=8, sticky="n")

    def register(self):
        firstname = self.firstname_input.get()
        lastname = self.lastname_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        password_check = self.password_check_input.get()
        print(User.create.__code__.co_varnames)

        if password_check == password:
            new_user = User()
            result = new_user.create(firstname, lastname, email, password)
            self.controller.set_user_in_frames(result)
            self.controller.show_frame("MainFrame") # Just to be quicker
            #self.controller.show_frame("UserConnectionFrame")