import customtkinter as ctk

class JanelaSubstituir(ctk.CTkToplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=0, padx=0, side=ctk.TOP, fill="x")

        self.title("Substituir")
        self.geometry("600x300")

        self.label = ctk.CTkLabel(self.frame, text="Localizar:")
        self.label.pack(pady=20, side = ctk.LEFT)

        self.entry = ctk.CTkEntry(self.frame, placeholder_text="Digite algo...")
        self.entry.pack(padx=10, side = ctk.LEFT)

        self.button = ctk.CTkButton(self.frame, text="Substituir")
        self.button.pack(pady=10,side = ctk.LEFT)
