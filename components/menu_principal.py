import tkinter as tk
from .menu_arquivo import MenuArquivo

class Menu(tk.Menu):
    def __init__(self, master=None, caixa_texto):
        super().__init__(master, tearoff=0)
        self.master = master
        self.caixa_texto = caixa_texto  
        menu_arquivo1 = MenuArquivo(self, caixa_texto=caixa_texto)
        self.add_cascade(label="Arquivo",menu=menu_arquivo1)