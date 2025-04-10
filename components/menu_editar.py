import tkinter as tk

class MenuEditar(tk.Menu):
    def __init__(self, master=None, caixa_texto=None):      
        super().__init__(master, tearoff=0)
        self.caixa_texto = caixa_texto
        self.add_cascade(label='Editar')
        self.add_command(label='Copiar', command=self.copiar)
        self.add_command(label='Colar', command=self.colar)
        self.add_command(label='Recortar', command=self.recortar)
        self.add_command(label='Limpar', command=self.limpar)
        self.add_command(label='Selecionar Tudo', command=self.selecionar_tudo)