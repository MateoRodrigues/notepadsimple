from pages.pageopen import janela_abrir_arquivo
from pages.pagesave import janela_salvar_arquivo
import os
class FileTxt:
    @staticmethod
    def abrir_arquivo_texto():
        abrir_endereco_arquivo_texto = janela_abrir_arquivo()
        with open(abrir_endereco_arquivo_texto, 'r+') as arquivo_texto:
             conteudo = arquivo_texto.read()
             return os.path.basename(arquivo_texto.name), conteudo, arquivo_texto.name
    @staticmethod
    def salvar_como_arquivo_texto(caixa_texto, pagina):
        salvar_endereco_arquivo_texto = janela_salvar_arquivo()
        if salvar_endereco_arquivo_texto:
            try:
                conteudo:str = caixa_texto
                with open(salvar_endereco_arquivo_texto, 'w', encoding='utf-8') as arquivo:
                    if conteudo is not None:
                        pagina.atualizar_titulo_da_página(os.path.basename(arquivo.name))
                        arquivo.write(conteudo)
            except Exception as e:
                print(f"Erro ao salvar arquivo: {e}")
    @staticmethod
    def salvar_arquivo_texto(caixa_texto, pagina,endereco_do_arquivo):
        titulo_da_pagina_atual = pagina.title()
        nome_arquivo = titulo_da_pagina_atual.split(" - ")[0].strip()
        with open(endereco_do_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(caixa_texto)
            
        





