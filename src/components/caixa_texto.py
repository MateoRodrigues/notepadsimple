import tkinter as tk
import re


class CaixaTexto(tk.Text):
    def __init__(self, master=None, *, pagina=None, **kwargs):
        super().__init__(
            master,
            wrap="word",
            font=("JetBrains Mono", 12),
            bg="#2B2B2B",  # Cor de fundo escura
            fg="white",  # Texto branco
            insertbackground="white",  # Cursor branco
            selectbackground="#1F538D",  # Seleção azul
            relief="flat",
        )
        self.bind("<<Modified>>", self.on_modified)
        self.pagina = pagina
        self._configure_highlight_tags()

    def set_caixa_texto(self, conteudo):
        self.delete(1.0, tk.END)
        self.insert(1.0, conteudo)

    def get_caixa_texto(self):
        conteudo = self.get(1.0, tk.END)
        return conteudo.strip()

    def clear_caixa_texto(self):
        self.delete(1.0, tk.END)

    def select_all(self):
        # Remove seleção anterior e seleciona tudo
        self.tag_add("sel", "1.0", "end-1c")
        self.mark_set("insert", "1.0")  # Move o cursor para o início
        self.see("insert")

    def paste(self):
        conteudo = self.clipboard_get()
        self.insert(tk.INSERT, conteudo)

    def on_modified(self, event=None):
        # Reseta a flag de modificação
        if self.edit_modified:
            t = self.pagina.title()
            self.pagina.title(f"*{t}")
            self.edit_modified(True)

    def _configure_highlight_tags(self):
        """Configura as tags padrão para destaque de palavras."""
        self.tag_config("destaque_amarelo", background="#FFFF00", foreground="#000000")
        self.tag_config("destaque_vermelho", background="#FF6B6B", foreground="white")
        self.tag_config("destaque_verde", background="#51CF66", foreground="#000000")
        self.tag_config("destaque_azul", background="#4ECDC4", foreground="#000000")
        self.tag_config("destaque_laranja", background="#FFB347", foreground="#000000")
        self.tag_config("destaque_roxo", background="#DDA0DD", foreground="#000000")

    def destacar_palavras(self, palavras, cor="destaque_amarelo", case_sensitive=False):
        """
        Destaca palavras específicas no texto.
        
        Args:
            palavras (str ou list): Palavra ou lista de palavras a destacar
            cor (str): Tag de cor (destaque_amarelo, destaque_vermelho, destaque_verde, 
                      destaque_azul, destaque_laranja, destaque_roxo)
            case_sensitive (bool): Se True, a busca é sensível a maiúsculas/minúsculas
        """
        # Remove destaque anterior
        self.tag_remove(cor, "1.0", tk.END)
        
        # Converte palavras em lista se for string
        if isinstance(palavras, str):
            palavras = [palavras]
        
        flags = 0 if case_sensitive else re.IGNORECASE
        
        # Para cada palavra, encontra e destaca todas as ocorrências
        for palavra in palavras:
            # Escapa caracteres especiais de regex
            palavra_escaped = re.escape(palavra)
            pattern = f"\\b{palavra_escaped}\\b"  # \b garante limites de palavra
            
            for match in re.finditer(pattern, self.get("1.0", tk.END), flags):
                start_idx = f"1.0 + {match.start()} chars"
                end_idx = f"1.0 + {match.end()} chars"
                self.tag_add(cor, start_idx, end_idx)

    def limpar_destaques(self, cor=None):
        """
        Remove destaques de palavras.
        
        Args:
            cor (str, optional): Se especificada, remove apenas destaques dessa cor.
                                Se None, remove todos os destaques.
        """
        cores_disponiveis = [
            "destaque_amarelo", "destaque_vermelho", "destaque_verde",
            "destaque_azul", "destaque_laranja", "destaque_roxo"
        ]
        
        if cor:
            self.tag_remove(cor, "1.0", tk.END)
        else:
            for cor_tag in cores_disponiveis:
                self.tag_remove(cor_tag, "1.0", tk.END)
