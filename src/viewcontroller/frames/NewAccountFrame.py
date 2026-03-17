import customtkinter as ctk

class NewAccountFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        ctk.CTkFrame.__init__(self, parent)
        
        label = ctk.CTkLabel(self, text ="New Account", font = ("Arial", 12, "bold"))
        
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
 
        main_menu_button = ctk.CTkButton(self, text ="Login",
        command = lambda : controller.show_frame("MainFrame"))
    
        main_menu_button.grid(row = 1, column = 1, padx = 10, pady = 10)
 
        user_connection_button = ctk.CTkButton(self, text ="User Connection",
        command = lambda : controller.show_frame("UserConnectionFrame"))
    
        user_connection_button.grid(row = 2, column = 1, padx = 10, pady = 10)