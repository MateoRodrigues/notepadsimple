import tkinter as tk
from .menu_arquivo import MenuArquivo

class MenuPrincipal(tk.Menu):
    def __init__(self, master=None, **kwargs):
        super().__init__(master,**kwargs)
        menu_arquivo1 = MenuArquivo(self, tearoff=0)
        self.add_cascade(label="Arquivo",menu=menu_arquivo1)