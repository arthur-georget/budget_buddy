import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, controller): 
        ctk.CTkFrame.__init__(self, parent)
        
        label = ctk.CTkLabel(self, text ="Main menu", font = ("Arial", 12, "bold"))
        
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
 
        history_button = ctk.CTkButton(self, text ="History",
        command = lambda : controller.show_frame("HistoryFrame"))
    
        history_button.grid(row = 1, column = 1, padx = 10, pady = 10)