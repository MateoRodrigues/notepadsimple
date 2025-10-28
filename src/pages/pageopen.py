from tkinter.filedialog import askopenfilename

def janela_abrir_arquivo():
    caminho_arquivo = askopenfilename(  
        title="Selecionar arquivo para abrir",
    filetypes=[
        ("Documentos", "*.txt"),
    ],
    initialdir="/home/matheus/Documentos/textos",
    initialfile="",
    defaultextension=".txt",)
    return caminho_arquivo
