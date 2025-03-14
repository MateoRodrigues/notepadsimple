import tkinter as tk

class MenuArquivo(tk.Menu):
    def __init__(self, master=None, **kwargs):
        super().__init__(master,**kwargs)
        self.add_cascade(label='Novo')
        self.add_command(label='Nova Janela')
        self.add_command(label='Abrir...')
        self.add_command(label='Salvar')
        self.add_command(label='Salvar Como...')