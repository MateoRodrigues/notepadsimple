import tkinter as tk

def titulo_pagina(arquivo=None) -> str:
    if arquivo == None:
        titulo_da_pagina = "Sem título - Bloco de Notas"
        return titulo_da_pagina
