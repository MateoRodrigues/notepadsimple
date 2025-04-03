import tkinter as tk
from services.filetxt import FileTxt

class CaixaTexto(tk.Text):
    def __init__(self,master=None, **kwargs):
        super().__init__(master,**kwargs)
    def set_caixa_texto(self):
        self.insert(1.0,FileTxt.abrir_arquivo_texto())
