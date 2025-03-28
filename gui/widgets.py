import tkinter as tk
from tkinter import ttk
from .styles import TokyoFistTheme

class ScaledFrame(ttk.Frame):
    """Frame that scales its children based on window size"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.width = 1
        self.height = 1
        
    def on_resize(self, event):
        # Update scaling factors
        self.width = event.width / 1000
        self.height = event.height / 800
        
        # Scale all child widgets
        for child in self.winfo_children():
            if hasattr(child, 'set_scaling'):
                child.set_scaling(self.width, self.height)

class HealthBar(tk.Canvas):
    def __init__(self, master, max_value, current_value, label, color=None, **kwargs):
        super().__init__(
            master,
            bg=TokyoFistTheme.COLORS['primary'],
            highlightthickness=0,
            height=30,
            **kwargs
        )
        self.max_value = max_value
        self.current_value = current_value
        self.label = label
        self.color = color or TokyoFistTheme.COLORS['accent']
        self.draw_bar()
        
    def draw_bar(self):
        self.delete('all')
        
        # Calculate dimensions
        width = self.winfo_width()
        height = self.winfo_height()
        ratio = min(1.0, max(0.0, self.current_value / self.max_value))
        bar_width = int(width * ratio)
        
        # Draw background
        self.create_rectangle(
            0, 0, width, height,
            fill=TokyoFistTheme.COLORS['secondary'],
            outline=''
        )
        
        # Draw health bar
        self.create_rectangle(
            0, 0, bar_width, height,
            fill=self.color,
            outline=''
        )
        
        # Draw text
        self.create_text(
            width/2, height/2,
            text=f"{self.label}: {self.current_value}/{self.max_value}",
            fill=TokyoFistTheme.COLORS['text'],
            font=TokyoFistTheme.FONTS['small']
        )
        
    def update_value(self, new_value):
        self.current_value = new_value
        self.draw_bar()
