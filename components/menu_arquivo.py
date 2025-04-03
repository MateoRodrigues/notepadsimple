import tkinter as tk
from services.filetxt import FileTxt

class MenuArquivo(tk.Menu):
    def __init__(self, master=None, **kwargs, caixa_texto:tk.Text):
        super().__init__(master, tearoff=0)
        self.add_cascade(label='Novo')
        self.add_command(label='Nova Janela')
        self.add_command(label='Abrir...', command=self.abrir_arquivo)
        self.add_command(label='Salvar')
        self.add_command(label='Salvar Como...')
    def abrir_arquivo(self):