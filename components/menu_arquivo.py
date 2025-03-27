import tkinter as tk
from services.filetxt import FileTxt

class MenuArquivo(tk.Menu):
    def __init__(self, master=None, **kwargs):
        super().__init__(master,**kwargs)
        self.add_cascade(label='Novo')
        self.add_command(label='Nova Janela')
        self.add_command(label='Abrir...', command=FileTxt.abrir_arquivo_texto)
        self.add_command(label='Salvar', command= FileTxt.salvar_arquivo_texto)
        self.add_command(label='Salvar Como...')