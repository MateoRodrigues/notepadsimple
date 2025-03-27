import tkinter as tk

class CaixaTexto(tk.Text):
    def __init__(self,master=None, **kwargs):
        super().__init__(master,**kwargs)
    def salvar_arquivo_texto(self):
        return self.get("1.0", tk.END).strip()