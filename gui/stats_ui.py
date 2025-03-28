import tkinter as tk
from tkinter import ttk

class TokyoFistTheme:
    COLORS = {
        'primary': '#2d2d2d',
        'secondary': '#3a3a3a',
        'accent': '#e74c3c',
        'text': '#ecf0f1',
        'highlight': '#3498db'
    }

    FONTS = {
        'title': ('Helvetica', 24, 'bold'),
        'header': ('Helvetica', 18),
        'body': ('Helvetica', 14),
        'small': ('Helvetica', 12)
    }

    @classmethod
    def configure_styles(cls):
        style = ttk.Style()
        
        # General style
        style.configure(
            'TFrame',
            background=cls.COLORS['primary']
        )
        
        # Button styles
        style.configure(
            'Primary.TButton',
            foreground=cls.COLORS['text'],
            background=cls.COLORS['accent'],
            font=cls.FONTS['body'],
            padding=10,
            borderwidth=0
        )
        
        style.map(
            'Primary.TButton',
            background=[('active', cls.COLORS['highlight'])]
        )
        
        # Label styles
        style.configure(
            'Header.TLabel',
            foreground=cls.COLORS['text'],
            background=cls.COLORS['primary'],
            font=cls.FONTS['header']
        )
        
        # Entry styles
        style.configure(
            'TEntry',
            fieldbackground=cls.COLORS['secondary'],
            foreground=cls.COLORS['text'],
            insertcolor=cls.COLORS['text'],
            padding=5
        )
