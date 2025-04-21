import tkinter as tk
from services.filetxt import FileTxt

class MenuArquivo(tk.Menu):
    def __init__(self, master=None, caixa_texto=None, pagina=None):      
        super().__init__(master, tearoff=0)
        self.pagina = pagina
        self.caixa_texto = caixa_texto
        self.add_cascade(label='Novo', accelerator="Ctrl+N")
        self.add_command(label='Nova Janela')
        self.add_command(label='Abrir...', accelerator="Ctrl+O", command=self.abrir_arquivo)
        self.add_command(label='Salvar', accelerator="Ctrl+S")
        self.add_command(label='Salvar Como...', command=self.salvar_arquivo)
    def abrir_arquivo(self):
        nome_arquivo,conteudo = FileTxt.abrir_arquivo_texto()
        self.pagina.atualizar_titulo_da_página(nome_arquivo)
        self.caixa_texto.set_caixa_texto(conteudo)
    def salvar_arquivo(self):
        conteudo = self.caixa_texto.get_caixa_texto()
        FileTxt.salvar_arquivo_texto(conteudo, self.pagina)
