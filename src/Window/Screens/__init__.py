from customtkinter import CTk, set_default_color_theme
from CTkListbox import *

set_default_color_theme("dark-blue")

class MainWindow:
    def __init__(self):
        app = CTk()
        app.title("Repositórios configurados")
        app.geometry("200x400")
        self.win = app
        
        self._build()
        
        app.protocol("WM_DELETE_WINDOW", lambda : self._close())
        app.mainloop()

    def _build(self):
        # override with build components in 'self.win'
        pass

    def _close(self):
        self.win.destroy()
    
    pass