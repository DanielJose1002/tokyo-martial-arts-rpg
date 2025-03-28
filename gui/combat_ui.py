import tkinter as tk
from tkinter import ttk
from .styles import TokyoFistTheme
from .widgets import HealthBar, ScaledFrame

class CombatUI(ScaledFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.setup_ui()
        
    def setup_ui(self):
        # Main grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=3)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Player info frame
        player_frame = ttk.Frame(self, style='TFrame')
        player_frame.grid(row=0, column=0, sticky='nsew')
        self.setup_character_display(player_frame, self.controller.player, is_player=True)
        
        # Combat log
        self.log_text = tk.Text(
            self,
            bg=TokyoFistTheme.COLORS['secondary'],
            fg=TokyoFistTheme.COLORS['text'],
            font=TokyoFistTheme.FONTS['small'],
            state='disabled',
            wrap=tk.WORD
        )
        self.log_text.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        
        # Actions frame
        actions_frame = ttk.Frame(self, style='TFrame')
        actions_frame.grid(row=2, column=0, sticky='nsew')
        self.setup_actions(actions_frame)
        
    def setup_character_display(self, parent, character, is_player):
        # Health bar
        health_bar = HealthBar(
            parent,
            max_value=character.max_hp,
            current_value=character.hp,
            label=f"{character.name} - HP"
        )
        health_bar.pack(fill=tk.X, padx=20, pady=10)
        
        # Stamina bar
        stamina_bar = HealthBar(
            parent,
            max_value=character.max_stamina,
            current_value=character.stamina,
            label=f"{character.name} - Stamina",
            color=TokyoFistTheme.COLORS['highlight']
        )
        stamina_bar.pack(fill=tk.X, padx=20, pady=(0, 20))
        
    def setup_actions(self, parent):
        # Style buttons
        style_buttons = ttk.Frame(parent)
        style_buttons.pack(fill=tk.X, padx=20, pady=10)
        
        for style in self.controller.player.available_styles:
            btn = ttk.Button(
                style_buttons,
                text=style.name,
                style='Primary.TButton',
                command=lambda s=style: self.controller.switch_style(s)
            )
            btn.pack(side=tk.LEFT, expand=True, padx=5)
        
        # Move buttons
        moves_frame = ttk.Frame(parent)
        moves_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create 2x2 grid of moves
        for i in range(2):
            moves_frame.grid_rowconfigure(i, weight=1)
            moves_frame.grid_columnconfigure(i, weight=1)
            
        moves = self.controller.player.current_style.moves
        for idx, move in enumerate(moves[:4]):  # Show first 4 moves
            row = idx // 2
            col = idx % 2
            btn = ttk.Button(
                moves_frame,
                text=f"{move.name}\n({move.stamina_cost} Stamina)",
                style='Primary.TButton',
                command=lambda m=move: self.controller.execute_move(m)
            )
            btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
