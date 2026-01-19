import tkinter as tk
import tkinter.font as tkFont
import os 
from components.menu_principal import Menu
from components.caixa_texto import CaixaTexto
from services.uteis import titulo_pagina
from pathlib import Path
import ttkbootstrap as ttk
from components.scroolbar_y import AutoHideScrollbar
from services.pagemain_bloc import PageMainControl


class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        ttk.Style("litera")
        self.pgmain_control = PageMainControl()
        self.geometry(self.pgmain_control.geometry)

        # Muda a fonte padrão do menu vertical
        self.fonte_sistema = tkFont.nametofont("TkMenuFont")
        self.fonte_sistema.configure(
            size=20,
            family="mincho",
            weight="bold",
        )
        # Ícone da aplicação
        caminho_icone = (
            Path(__file__).parent.parent.parent / "assets" / "ChatGPT-preto-branco.png"
        )
        icon = tk.PhotoImage(file=str(caminho_icone))
        self.iconphoto(True, icon)
        # Titulo da página
        self.title(titulo_pagina())
        self.sep = ttk.ttk.Separator(self, orient="horizontal", bootstyle="dark")

        # Configurações da caixa de texto
        self.caixa_texto = CaixaTexto(self, pagina=self)
        self.menu = Menu(
            self,
            self.caixa_texto,
        )
        self.scrollbar = AutoHideScrollbar(
            self.caixa_texto,
            orient="vertical",
            command=self.caixa_texto.yview,
            bootstyle="dark-round",
        )
        # Configurações da ordem da página
        self.config(menu=self.menu)
        self.sep.pack(side=tk.TOP, fill="x")
        self.caixa_texto.pack(side=tk.BOTTOM, expand=True, fill="both")
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.caixa_texto.configure(yscrollcommand=self.scrollbar.set)

    def atualizar_titulo_da_página(self, nome_arquivo=None):
        if nome_arquivo is None:
            self.title(titulo_pagina())
        else:
            self.title(titulo_pagina(nome_arquivo))
