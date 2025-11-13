import tkinter as tk
import tkinter.font as tkFont
from pages.pagereplace import JanelaSubstituir

class MenuFormatar(tk.Menu):
    def __init__(self, master=None, pagina=None):      
        super().__init__(master, tearoff=0,bg='white',activebackground="lightblue",activeforeground="black")
        self.janelasubstituir = JanelaSubstituir
        self.pagina = pagina
        self.menu_fonte = tk.Menu(self, tearoff=0)
        for fonte in sorted(tkFont.families()):
            self.menu_fonte.add_command(label=fonte, command=self.alterar_fonte)
        self.add_cascade(label='Fonte...', menu=self.menu_fonte)
        self.add_command(label='Codificar')
        self.add_command(label='Substituir', command=self.substituir)

    def substituir(self):
        self.janelasubstituir(self.pagina)
    def alterar_fonte(self):
        pass


   