import tkinter as tk


class CaixaTexto(tk.Text):
    def __init__(self, master=None, *, pagina=None, **kwargs):
        super().__init__(
            master,
            wrap="word",
            font=("mincho", 12),
            bg="#2B2B2B",  # Cor de fundo escura
            fg="white",  # Texto branco
            insertbackground="white",  # Cursor branco
            selectbackground="#1F538D",  # Seleção azul
            relief="flat",
        )
        self.bind("<<Modified>>", self.on_modified)
        self.pagina = pagina

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
