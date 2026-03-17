import customtkinter as ctk

class HistoryFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        ctk.CTkFrame.__init__(self, parent)
        
        label = ctk.CTkLabel(self, text ="History", font = ("Arial", 12, "bold"))
        
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
 
        main_button = ctk.CTkButton(self, text ="Main menu",
        command = lambda : controller.show_frame("MainFrame"))
    
        main_button.grid(row = 1, column = 1, padx = 10, pady = 10)