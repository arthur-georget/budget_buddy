import customtkinter as ctk
from src.viewcontroller.frames.UserConnectionFrame import UserConnectionFrame
from src.viewcontroller.frames.NewUserFrame import NewUserFrame
from src.viewcontroller.frames.MainFrame import MainFrame
from src.viewcontroller.frames.TransactionsRecordFrame import TransactionsRecordFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Budget Buddy")
        self.geometry("900x650")
        
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (UserConnectionFrame, NewUserFrame, MainFrame, TransactionsRecordFrame):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("UserConnectionFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        frame.focus_force()