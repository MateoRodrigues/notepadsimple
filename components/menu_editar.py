import tkinter as tk

class MenuEditar(tk.Menu):
    def __init__(self, master=None):      
        super().__init__(master, tearoff=0,bg='white',activebackground="lightblue",activeforeground="black")
        self.add_cascade(label='Editar')
        self.add_command(label='Copiar')
        self.add_command(label='Colar')
        self.add_command(label='Recortar')
        self.add_command(label='Limpar')
        self.add_command(label='Selecionar Tudo')