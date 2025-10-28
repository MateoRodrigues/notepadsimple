import os
import tkinter as tk
import tkinter.font as tkFont
from components.menu_principal import Menu
from components.caixa_texto import CaixaTexto
from services.uteis import titulo_pagina

class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x500")

        # Muda a fonte padrão do menu vertical

        self.fonte_menu = tkFont.Font(family="CCourier New", size=12)
        self.option_add("*Menu*Font", self.fonte_menu)

        # Buscando o ícone nos arquivos
        caminho_base = os.path.dirname(__file__)
        caminho_icone = os.path.join(caminho_base, "../assets/iconelinux.png")
        icon = tk.PhotoImage(file=caminho_icone)
        self.iconphoto(True, icon)
        #Titulo da página
        self.title(titulo_pagina())

        # Configurações da caixa de texto
        self.fonte_caixa_texto = tkFont.Font(family="Arial", size=12)
        self.caixa_texto = CaixaTexto(self, font=self.fonte_caixa_texto)
        self.menu = Menu(self, self.caixa_texto)
        # Configurações da ordem da página
        self.config(menu=self.menu)
        self.caixa_texto.pack(side=tk.BOTTOM,expand=True,fill='both')

    def atualizar_titulo_da_página(self, nome_arquivo=None):
        if nome_arquivo == None:
            self.title(titulo_pagina())
        else:
            self.title(titulo_pagina(nome_arquivo))
     
   

            

        