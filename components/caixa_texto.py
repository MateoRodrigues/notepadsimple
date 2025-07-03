import tkinter as tk

class CaixaTexto(tk.Text):
    def __init__(self,master=None, **kwargs):
        super().__init__(master,**kwargs)
    def set_caixa_texto(self,conteudo):
        self.delete(1.0,tk.END)
        self.insert(1.0,conteudo)
    def get_caixa_texto(self):
        conteudo = self.get(1.0,tk.END)
        return conteudo.strip()
    def clear_caixa_texto(self):
        self.delete(1.0, tk.END)
    def select_all(self):
        # Remove seleção anterior e seleciona tudo
        self.tag_add("sel", "1.0", "end-1c")
        self.mark_set("insert", "1.0")  # Move o cursor para o início
        self.see("insert") 
    def paste(self):
        conteudo = self.clipboard_get()
        self.insert(tk.INSERT, conteudo)
