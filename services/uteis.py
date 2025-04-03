import tkinter as tk
from services.filetxt import FileTxt
def caixa_para_arquivo(caixa_texto: tk.Text):
    arquivo_texto =caixa_texto.get("1.0", tk.END)
    return arquivo_texto

def arquivo_para_caixa():
    pass



def titulo_pagina(titulo_da_pagina="Sem título - Bloco de Notas"):
    return titulo_da_pagina