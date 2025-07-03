import tkinter as tk

class MenuEditar(tk.Menu):
    def __init__(self, master=None, caixa_texto=None):      
        super().__init__(master, tearoff=0,bg='white',activebackground="lightblue",activeforeground="black")
        self.caixa_texto = caixa_texto


        self.add_cascade(label='Editar')
        self.add_command(label='Copiar')
        self.add_command(label='Colar', accelerator='Ctrl+V', command=self.colar)
        self.add_command(label='Recortar')
        self.add_command(label='Limpar')
        self.add_command(label='Selecionar Tudo', accelerator='Ctrl+A', command=self.selecionar_tudo)

    def selecionar_tudo(self):
        self.caixa_texto.select_all()
    def colar(self):
        self.caixa_texto.paste()