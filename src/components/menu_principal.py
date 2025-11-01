import tkinter as tk
from .menu_arquivo import MenuArquivo
from .menu_editar import MenuEditar
from .menu_formatar import MenuFormatar

class Menu(tk.Menu):
    def __init__(self,master=None, caixa_texto=None, fonte=None):
        #self.fonte_tupla = (fonte.actual()['family'], fonte.actual()['size'], 'bold')
        super().__init__(master, tearoff=0,)
        self.master = master
        self.caixa_texto = caixa_texto  
        menu_arquivo1 = MenuArquivo(self, caixa_texto=caixa_texto,pagina=master)
        menu_editar1 = MenuEditar(self, caixa_texto=caixa_texto, pagina=master)
        menu_formatar1 = MenuFormatar(self, pagina=master)
        self.add_cascade(label="Arquivo",menu=menu_arquivo1)
        self.add_cascade(label="Editar",menu=menu_editar1)
        self.add_cascade(label="Formatar",menu=menu_formatar1)
