import customtkinter as ctk

class JanelaSubstituir(ctk.CTkToplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.title("Substituir")
        self.geometry("600x300")

        self.label = ctk.CTkLabel(self, text="Sou uma janela do CustomTkinter")
        self.label.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="Digite algo...")
        self.entry.pack(pady=5)

        self.button = ctk.CTkButton(self, text="Fechar", command=self.destroy)
        self.button.pack(pady=10)
