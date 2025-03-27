from pages.pageopen import janela_abrir_arquivo
from pages.pagesave import janela_salvar_arquivo
class FileTxt:
    @staticmethod
    def abrir_arquivo_texto():
        abrir_endereco_arquivo_texto = janela_abrir_arquivo()
    @staticmethod
    def salvar_arquivo_texto(caixa_texto):
        salvar_endereco_arquivo_texto = janela_salvar_arquivo()
        if salvar_endereco_arquivo_texto:
            try:
                conteudo:str = caixa_texto
                with open(salvar_endereco_arquivo_texto, 'w', encoding='utf-8') as arquivo:
                    if conteudo is not None:
                        arquivo.write(conteudo)
            except Exception as e:
                print(f"Erro ao salvar arquivo: {e}")
                return False




