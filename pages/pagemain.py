import tkinter as tk
from components.menu_principal import Menu
from components.caixa_texto import CaixaTexto
from services.uteis import titulo_pagina
class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x500")
        # Buscando o ícone nos arquivos
        self.iconbitmap("C:/Users/mateo/Documents/python/notepadsimple/assets/Double-J-Design-Origami-Notepad.ico")
        self.title(titulo_pagina())
        self.caixa_texto = CaixaTexto(self)
        self.menu = Menu(self, self.caixa_texto)
        self.config(menu=self.menu)
        self.caixa_texto.pack(side=tk.BOTTOM,expand=True,fill='both')
    def atualizar_titulo_da_página(self, nome_arquivo=None):
        if nome_arquivo == None:
            self.title(titulo_pagina())
        else:
            self.title(titulo_pagina(nome_arquivo))
   

            

        