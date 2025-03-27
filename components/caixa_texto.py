import tkinter as tk
from services.filetxt import FileTxt

class CaixaTexto(tk.Text):
    def __init__(self,master=None, **kwargs):
        super().__init__(master,**kwargs)
    def salvar_arquivo_texto(self):
        FileTxt.salvar_arquivo_texto(self.get("1.0","end").strip())