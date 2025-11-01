import tkinter as tk
import tkinter.font as tkFont

# Adicione isso no seu __init__ após criar o menu:
fonte_atual = tkFont.nametofont("TkDefaultFont")
print(f"Fonte do sistema: {fonte_atual.actual()}")