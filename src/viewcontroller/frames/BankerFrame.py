import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.model.User import User
from src.viewcontroller.frames.ScrollableUsersFrame import ScrollableUsersFrame

class BankerFrame(ctk.CTkFrame):

    def __init__(self, parent, controller, user):
        ctk.CTkFrame.__init__(self, parent)

        self.controller = controller
        self.__user = user

        self.label = ctk.CTkLabel(self, text="Banker Management Console", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        self.scrollable_users = ScrollableUsersFrame(self)
        self.scrollable_users.pack(pady=10, padx=20, fill="both", expand=True)

        self.button_container = ctk.CTkFrame(self, fg_color="transparent")
        self.button_container.pack(pady=20)

        self.new_bank_account_button = ctk.CTkButton(
            self.button_container, 
            text="Create New Account",
            command=self._on_create_account
        )
        self.new_bank_account_button.grid(row=0, column=0, padx=10)

        self.delete_bank_account_button = ctk.CTkButton(
            self.button_container, 
            text="Delete Selected Account",
            fg_color="#cc0000",
            hover_color="#8B0000",
            command=self._on_delete_account
        )
        self.delete_bank_account_button.grid(row=0, column=1, padx=10)

        self.back_button = ctk.CTkButton(
            self, 
            text="Return to Main Menu", 
            command=lambda: self.controller.show_frame("MainFrame")
        )
        self.back_button.pack(side="bottom", pady=10)

    def _on_create_account(self):
        CTkMessagebox(title="Success", message="New bank account created.", icon="check")

    def _on_delete_account(self):
        msg = CTkMessagebox(
            title="Warning", 
            message="Are you sure?",
            icon="warning", 
            option_1="Cancel", 
            option_2="Delete"
        )
        if msg.get() == "Delete":
            CTkMessagebox(title="Deleted", message="Account removed.", icon="info")

    def set_user(self, user: User):
        self.__user = user
        print(f"BankerFrame: {self.__user.get_email()}")