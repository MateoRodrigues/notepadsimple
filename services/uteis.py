import tkinter as tk

def titulo_pagina(nome_arquivo=None) -> str:
    if nome_arquivo == None:
        titulo_da_pagina = "Sem título - Bloco de Notas"
        return titulo_da_pagina
    else:
        titulo_da_pagina = f"{nome_arquivo} - Bloco de Notas"
        return titulo_da_pagina