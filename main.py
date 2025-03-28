import tkinter as tk
from tkinter import ttk
from gui import TokyoFistTheme
from gui.main_menu import MainMenu
from gui.combat_ui import CombatUI

class TokyoFistApp:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.current_frame = None
        
        # Sample player data (will be replaced with real implementation)
        self.player = {
            'name': 'Player',
            'hp': 100,
            'max_hp': 100,
            'stamina': 100,
            'max_stamina': 100
        }
        
        self.show_main_menu()
        
    def setup_window(self):
        self.root.title("Tokyo Fist")
        TokyoFistTheme.configure_styles()
        
        # Set window size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        self.root.geometry(f"{window_width}x{window_height}")
        
        # Make window resizable
        self.root.minsize(800, 600)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def show_main_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = MainMenu(self.root, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
    def start_new_game(self):
        # Transition to combat screen for demo purposes
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = CombatUI(self.root, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
    def load_game(self):
        print("Load game functionality would go here")
        
    def show_options(self):
        print("Options menu would go here")
        
    def quit_game(self):
        self.root.quit()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TokyoFistApp()
    app.run()
