import tkinter as tk
from ..pages. import JanelaSubstituir

class MenuFormatar(tk.Menu):
    def __init__(self, master=None, pagina=None):      
        super().__init__(master, tearoff=0,bg='white',activebackground="lightblue",activeforeground="black")
        self.janelasubstituir = JanelaSubstituir
        self.pagina = pagina
        self.add_cascade(label='Formatar')
        self.add_command(label='Fonte...')
        self.add_command(label='Codificar')
        self.add_command(label='Substituir', command=self.substituir)

    def substituir(self):
        self.janelasubstituir(self.pagina)


   