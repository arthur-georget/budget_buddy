import customtkinter as ctk
from src.model.User import User
from CTkMessagebox import CTkMessagebox

class UserConnectionFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, user): 
        ctk.CTkFrame.__init__(self, parent)

        self.controller = controller
        self.__user = user
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 6), weight=1)

        ctk.CTkLabel(self, text="Budget Buddy", font=("Arial", 32, "bold"), text_color="#1f538d").grid(row=1, pady=(0, 10))
        ctk.CTkLabel(self, text="Welcome back!", font=("Arial", 14)).grid(row=2, pady=(0, 30))

        self.email_input = ctk.CTkEntry(self, placeholder_text="Email", width=300, height=45)
        self.email_input.grid(row=3, pady=10)

        self.password_input = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=300, height=45)
        self.password_input.grid(row=4, pady=10)

        ctk.CTkButton(self, text="Login", width=300, height=50, font=("Arial", 16, "bold"),
                      command=self.login).grid(row=5, pady=(30, 10))

        ctk.CTkButton(self, text="Create new account", fg_color="transparent", border_width=1,
                      command=lambda: controller.show_frame("NewUserFrame")).grid(row=6, sticky="n")

    def login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        user = User()
        result = user.login(password, email)
        if isinstance(result, User) and result.get_is_admin() == 'True':
            self.controller.show_frame("BankerFrame")
        elif isinstance(result, User):
            #user = User()
            #user.read(1)
            self.controller.set_user_in_frames(result)
            self.controller.show_frame("MainFrame")
        else:
            CTkMessagebox(title="Login Error", message="Invalid credentials.", icon="warning")