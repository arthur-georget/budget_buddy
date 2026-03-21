import customtkinter as ctk
from functools import partial

class ScrollableFilterFrame(ctk.CTkScrollableFrame):

    def __init__(self, parent, filters: list, title: str, radio: bool = False, **kwargs):

        ctk.CTkScrollableFrame.__init__(self, parent, label_text=title, **kwargs)

        self.__parent = parent

        self.__radio = radio

        self._scrollbar.configure(height=0)
        
        if self.__radio:
            self.__radio_var = ctk.StringVar(value="")
            for i,filter in enumerate(filters):
                filter_button = ctk.CTkRadioButton(self, text=filter, variable= self.__radio_var, value=filter)
                filter_button.grid(row=i, column=0, sticky="W", pady=5)
        else:        
            for i,filter in enumerate(filters):
                filter_button = ctk.CTkButton(self, text=filter, command= partial(self.__filter_action,filter), width=20)
                filter_button.grid(row=i, column=0, sticky="W", pady=5)
            
        self.__selected_filter = None


    def __filter_action(self, filter: str | None):
        self.__selected_filter = filter
        self.__parent.filter_action(None)
    
    def get_selected_filter(self):
        if self.__radio:
            self.__selected_filter = self.__radio_var.get()
        return self.__selected_filter