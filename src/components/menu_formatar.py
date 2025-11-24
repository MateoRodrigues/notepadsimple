import tkinter as tk
import tkinter.font as tkFont
from pages.pagereplace import JanelaSubstituir

class MenuFormatar(tk.Menu):
    def __init__(self, master=None, pagina=None):      
        super().__init__(master, tearoff=0)
        self.janelasubstituir = JanelaSubstituir
        self.pagina = pagina
        self.menu_fonte = tk.Menu(self, tearoff=0)
        # Adiciona as fontes disponíveis ao submenu de fontes
        for fonte in sorted(tkFont.families()):
            # Adiciona cada fonte como um comando no submenu e define a ação ao ser selecionada
            self.menu_fonte.add_command(label=fonte, command=lambda f=fonte: self.alterar_fonte(f))
        self.add_cascade(label='Fonte...', menu=self.menu_fonte)
        self.add_command(label='Substituir', command=self.substituir)

    def alterar_fonte(self, fonte):
        print(fonte)
    def substituir(self):
        self.janelasubstituir(self.pagina)


   