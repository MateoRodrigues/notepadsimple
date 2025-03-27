import tkinter as tk
from services.uteis import salvar_texto_caixa

class MenuArquivo(tk.Menu):
    def __init__(self, master=None, **kwargs):
        super().__init__(master,**kwargs)
        self.add_cascade(label='Novo')
        self.add_command(label='Nova Janela')
        self.add_command(label='Abrir...')
        self.add_command(label='Salvar')
        self.add_command(label='Salvar Como...', command= salvar_texto_caixa)