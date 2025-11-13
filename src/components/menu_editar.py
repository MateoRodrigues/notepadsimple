import tkinter as tk

class MenuEditar(tk.Menu):
    def __init__(self, master=None, caixa_texto=None, pagina=None):      
        super().__init__(master, tearoff=0,bg='white',activebackground="lightblue",activeforeground="black")
        self.caixa_texto = caixa_texto
        self.pagina = pagina
        self.add_command(label='Copiar', accelerator='Ctrl+C', command=self.copiar)
        self.add_command(label='Colar', accelerator='Ctrl+V', command=self.colar)
        self.add_command(label='Recortar')
        self.add_command(label='Limpar',command=self.limpar)
        self.add_command(label='Selecionar Tudo', accelerator='Ctrl+A', command=self.selecionar_tudo)

    def selecionar_tudo(self):
        self.caixa_texto.select_all()
    def colar(self):
        self.caixa_texto.paste()
    def limpar(self):
        self.caixa_texto.clear_caixa_texto()
    def copiar(self):
        self.pagina.clipboard_clear()
        self.pagina.clipboard_append(self.caixa_texto.get_caixa_texto())