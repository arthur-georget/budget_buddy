import customtkinter as ctk
from src.viewcontroller.frames.UserConnectionFrame import UserConnectionFrame
from src.viewcontroller.frames.NewUserFrame import NewUserFrame
from src.viewcontroller.frames.MainFrame import MainFrame
from src.viewcontroller.frames.TransactionsRecordFrame import TransactionsRecordFrame
from src.viewcontroller.frames.BankerFrame import BankerFrame
from src.viewcontroller.frames.GraphFrame import GraphFrame

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        self.title("Budget Buddy")
        self.geometry("1000x700")

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.current_user = None

        for FrameClass in (
            UserConnectionFrame, 
            NewUserFrame, 
            MainFrame, 
            TransactionsRecordFrame,
            BankerFrame,
            GraphFrame
        ):
            frame_instance = FrameClass(container, self, self.current_user)
            self.frames[FrameClass.__name__] = frame_instance
            frame_instance.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("BankerFrame")

    def show_frame(self, frame_class_name : str):
        frame = self.frames[frame_class_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()