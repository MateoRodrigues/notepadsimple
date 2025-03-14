from tkinter.filedialog import askopenfilename

def janela_abrir_arquivo():
    caminho_arquivo = askopenfilename()
    return caminho_arquivo
