import tkinter as tk
from components.menu_principal import MenuPrincipal
from components.caixa_texto import CaixaTexto

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x500")
        # Buscando o ícone nos arquivos
        self.iconbitmap("C:/Users/mateo/Documents/python/notepadsimple/assets/Double-J-Design-Origami-Notepad.ico")
        self.titulo_da_pagina = "Sem título - Bloco de Notas"
        self.title(self.titulo_da_pagina)
        self.menu = MenuPrincipal(self)
        self.config(menu=self.menu)
        self.caixa_texto = CaixaTexto(self)
        self.caixa_texto.pack(side=tk.BOTTOM,expand=True,fill='both')