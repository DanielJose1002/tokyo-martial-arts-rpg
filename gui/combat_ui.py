import tkinter as tk
from tkinter import ttk
from ...game.combat.core import Combatant
from ..styles import TokyoFistTheme
from ..widgets import HealthBar, ScaledFrame

class CombatUI(ScaledFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.setup_ui()
        
    def setup_ui(self):
        # Main grid layout
        self.grid_rowconfigure(0, weight=1)  # Player info
        self.grid_rowconfigure(1, weight=3)  # Combat log
        self.grid_rowconfigure(2, weight=1)  # Style selection
        self.grid_rowconfigure(3, weight=2)  # Moves
        self.grid_columnconfigure(0, weight=1)
        
        # Player info
        self.player_frame = ttk.Frame(self, style='TFrame')
        self.player_frame.grid(row=0, column=0, sticky='nsew')
        self.setup_character_display(self.player_frame, self.controller.player)
        
        # Enemy info
        self.enemy_frame = ttk.Frame(self, style='TFrame')
        self.enemy_frame.grid(row=0, column=1, sticky='nsew')
        self.setup_character_display(self.enemy_frame, self.controller.enemy)
        
        # Combat log
        self.log_text = tk.Text(
            self,
            bg=TokyoFistTheme.COLORS['secondary'],
            fg=TokyoFistTheme.COLORS['text'],
            font=TokyoFistTheme.FONTS['small'],
            state='disabled',
            wrap=tk.WORD
        )
        self.log_text.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
        
        # Style selection
        self.style_frame = ttk.Frame(self, style='TFrame')
        self.style_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')
        self.setup_style_buttons()
        
        # Moves
        self.moves_frame = ttk.Frame(self, style='TFrame')
        self.moves_frame.grid(row=3, column=0, columnspan=2, sticky='nsew')
        self.setup_move_buttons()
        
    def setup_style_buttons(self):
        ttk.Label(
            self.style_frame,
            text="Select Fighting Style:",
            style='Header.TLabel'
        ).pack(pady=5)
        
        buttons_frame = ttk.Frame(self.style_frame)
        buttons_frame.pack()
        
        for style in self.controller.player.available_styles:
            btn = ttk.Button(
                buttons_frame,
                text=style.name,
                style='Primary.TButton',
                command=lambda s=style: self.controller.switch_style(s)
            )
            btn.pack(side=tk.LEFT, expand=True, padx=5, pady=5)
    
    def setup_move_buttons(self):
        # Clear existing buttons
        for widget in self.moves_frame.winfo_children():
            widget.destroy()
            
        # Create 2x2 grid of moves
        for i in range(2):
            self.moves_frame.grid_rowconfigure(i, weight=1)
            self.moves_frame.grid_columnconfigure(i, weight=1)
            
        moves = self.controller.player.current_style.get_available_moves(
            self.controller.player.level
        )[:4]  # Show first 4 moves
        
        for idx, move in enumerate(moves):
            row = idx // 2
            col = idx % 2
            btn = ttk.Button(
                self.moves_frame,
                text=f"{move.name}\nDMG: {move.base_damage} | STAM: {move.stamina_cost}",
                style='Primary.TButton',
                command=lambda m=move: self.controller.execute_move(m)
            )
            btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
