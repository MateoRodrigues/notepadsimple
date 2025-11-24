from tkinter import filedialog


def janela_salvar_arquivo():
    endereco_arquivo_texto = filedialog.asksaveasfilename(
        # Título da janela de diálogo
        title="Salvar Arquivo",
        # Tipos de arquivo para filtrar (extensões)
        filetypes=[
            ("Arquivos de Texto", "*.txt"),
        ],
        # Pasta onde vai salvar
        initialdir="/home/matheus/Documentos/textos",
        # Nome inicial do arquivo
        initialfile="documento.txt",
        # Extensão padrão se não for especificada
        defaultextension=".txt",
        # Impede que o usuário cancele sem selecionar
        # (retorna string vazia se cancelar)
        # confirmoverwrite=True
    )

    return endereco_arquivo_texto
