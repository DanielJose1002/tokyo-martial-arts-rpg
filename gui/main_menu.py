import tkinter as tk
from tkinter import ttk
from .styles import TokyoFistTheme
from .widgets import ScaledFrame

class MainMenu(ScaledFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        container = ttk.Frame(self, style='TFrame')
        container.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)
        
        # Title
        title = ttk.Label(
            container,
            text="TOKYO FIST",
            style='Header.TLabel'
        )
        title.pack(pady=(0, 40))
        
        # Buttons frame
        buttons_frame = ttk.Frame(container)
        buttons_frame.pack()
        
        # Menu buttons
        buttons = [
            ("New Game", self.controller.start_new_game),
            ("Continue", self.controller.load_game),
            ("Options", self.controller.show_options),
            ("Exit", self.controller.quit_game)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(
                buttons_frame,
                text=text,
                style='Primary.TButton',
                command=command
            )
            btn.pack(fill=tk.X, pady=5, ipady=10)
