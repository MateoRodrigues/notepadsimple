import tkinter as tk
from services.filetxt import FileTxt

class MenuArquivo(tk.Menu):
    def __init__(self, master=None, caixa_texto=None):      
        super().__init__(master, tearoff=0)
        self.caixa_texto = caixa_texto
        self.add_cascade(label='Novo')
        self.add_command(label='Nova Janela')
        self.add_command(label='Abrir...', command=self.abrir_arquivo)
        self.add_command(label='Salvar')
        self.add_command(label='Salvar Como...')
    def abrir_arquivo(self):
        conteudo = FileTxt.abrir_arquivo_texto()
        self.caixa_texto.set_caixa_texto(conteudo)
