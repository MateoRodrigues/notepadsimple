import tkinter as tk
from services.filetxt import FileTxt

class MenuArquivo(tk.Menu):
    def __init__(self, master=None, caixa_texto=None, pagina=None):      
        super().__init__(master, tearoff=0,bg='white',activebackground="lightblue",activeforeground="black")
        
        # Pagina é a janela principal
        # caixa_texto é a caixa de texto onde o usuário escreve
        self.pagina = pagina
        self.caixa_texto = caixa_texto

        #Botões do menu Arquivo
        self.add_cascade(label='Novo', accelerator="Ctrl+N", command=self.novo_arquivo)
        self.add_command(label='Nova Janela',accelerator='Ctrl+Shift+N')
        self.add_command(label='Abrir...', accelerator="Ctrl+O", command=self.abrir_arquivo)
        self.add_command(label='Salvar', accelerator="Ctrl+S", command=self.salvar_arquivo)
        self.add_command(label='Salvar Como...', accelerator='Ctrl+Shift+S',command=self.salvar_como_arquivo)

    def abrir_arquivo(self):
        nome_arquivo,conteudo,self.endereco_do_arquivo = FileTxt.abrir_arquivo_texto()
        self.pagina.atualizar_titulo_da_página(nome_arquivo)
        self.caixa_texto.set_caixa_texto(conteudo)
    def salvar_como_arquivo(self):
        conteudo = self.caixa_texto.get_caixa_texto()
        FileTxt.salvar_como_arquivo_texto(conteudo, self.pagina)
    def salvar_arquivo(self):
        titulo_da_pagina_atual = self.pagina.title()
        if titulo_da_pagina_atual == 'Sem título - Bloco de Notas':
            self.salvar_como_arquivo()
        else:
            conteudo = self.caixa_texto.get_caixa_texto()
            FileTxt.salvar_arquivo_texto(conteudo, self.pagina,self.endereco_do_arquivo)
    def novo_arquivo(self):
        self.pagina.atualizar_titulo_da_página()
        self.caixa_texto.clear_caixa_texto()

