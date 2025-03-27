import tkinter as tk
from tkinter import filedialog


def exemplo_salvar_arquivo():
    endereco_arquivo_texto = filedialog.asksaveasfilename(
        # Título da janela de diálogo
        title='Salvar Arquivo',


        # Tipos de arquivo para filtrar (extensões)
        filetypes=[
            ('Arquivos de Texto', '*.txt'),
        ],

        # Nome inicial do arquivo
        initialfile='documento.txt',

        # Extensão padrão se não for especificada
        defaultextension='.txt',

        # Impede que o usuário cancele sem selecionar
        # (retorna string vazia se cancelar)
        # confirmoverwrite=True
    )

    return endereco_arquivo_texto


# Criar janela raiz (necessária para diálogos Tkinter)
root = tk.Tk()
root.withdraw()  # Oculta a janela principal

# Chama a função de exemplo
exemplo_salvar_arquivo()