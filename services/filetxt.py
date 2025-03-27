from pages.pageopen import janela_abrir_arquivo
from pages.pagesave import janela_salvar_arquivo
from components.caixa_texto import CaixaTexto
class FileTxt:
    @staticmethod
    def abrir_arquivo_texto():
        abrir_endereco_arquivo_texto = janela_abrir_arquivo()
        print(abrir_endereco_arquivo_texto)
    @staticmethod
    def salvar_arquivo_texto():
        salvar_endereco_arquivo_texto = janela_salvar_arquivo()
        print(salvar_endereco_arquivo_texto)




