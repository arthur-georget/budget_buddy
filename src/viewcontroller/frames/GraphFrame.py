import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphFrame(ctk.CTkFrame):
    def __init__(self, parent, controller, user):
        super().__init__(parent)
        self.controller = controller
        self.user = user

        self.label = ctk.CTkLabel(self, text="Financial Analytics", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        self.chart_container = ctk.CTkFrame(self, fg_color="transparent")
        self.chart_container.pack(pady=10, padx=20, fill="both", expand=True)
        
        self._render_graph()

        self.button_container = ctk.CTkFrame(self, fg_color="transparent")
        self.button_container.pack(pady=20)

        self.refresh_button = ctk.CTkButton(
            self.button_container, 
            text="Refresh Data",
            command=self._on_refresh
        )
        self.refresh_button.grid(row=0, column=0, padx=10)

        self.back_button = ctk.CTkButton(
            self, 
            text="Back to Dashboard", 
            command=lambda: self.controller.show_frame("MainFrame")
        )
        self.back_button.pack(side="bottom", pady=10)

    def _render_graph(self):
        for widget in self.chart_container.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
        fig.patch.set_facecolor('#2b2b2b')
        ax.set_facecolor('#2b2b2b')

        categories = ['Rent', 'Food', 'Transport', 'Leisure', 'Savings']
        values = [800, 300, 150, 200, 400]

        ax.bar(categories, values, color='#1f538d')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('white')

        canvas = FigureCanvasTkAgg(fig, master=self.chart_container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def _on_refresh(self):
        self._render_graph()