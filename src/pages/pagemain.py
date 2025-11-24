import os
import tkinter as tk
import tkinter.font as tkFont
from components.menu_principal import Menu
from components.caixa_texto import CaixaTexto
from services.uteis import titulo_pagina
from pathlib import Path
import ttkbootstrap as ttk

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        ttk.Style("litera")

        self.geometry("1000x500")

        # Muda a fonte padrão do menu vertical
        self.fonte_sistema = tkFont.nametofont("TkMenuFont")
        self.fonte_sistema.configure(size=20, family='newspaper', weight="bold",)
        # Ícone da aplicação
        caminho_icone = Path(__file__).parent.parent.parent / "assets" / "iconelinux.png"
        icon = tk.PhotoImage(file=str(caminho_icone))
        self.iconphoto(True, icon)
        #Titulo da página
        self.title(titulo_pagina())

        # Configurações da caixa de texto
        self.fonte_caixa_texto = tkFont.Font(family="Arial", size=12)
        self.caixa_texto = CaixaTexto(self, pagina = self)
        self.menu = Menu(self, self.caixa_texto,)
        # Configurações da ordem da página
        self.config(menu=self.menu)
        self.caixa_texto.pack(side=tk.BOTTOM,expand=True,fill='both')

    def atualizar_titulo_da_página(self, nome_arquivo=None):
        if nome_arquivo == None:
            self.title(titulo_pagina())
        else:
            self.title(titulo_pagina(nome_arquivo))
     
   

            

        