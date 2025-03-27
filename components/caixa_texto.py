import tkinter as tk
from services.filetxt import FileTxt
from services.uteis import salvar_texto_caixa

class CaixaTexto(tk.Text):
    def __init__(self,master=None, **kwargs):
        super().__init__(master,**kwargs)
    def salvar_arquivo_texto(self):
        if salvar:= salvar_texto_caixa() == True:
            FileTxt.salvar_arquivo_texto(self.get("1.0","end").strip())