import customtkinter as ctk

class JanelaSubstituir(ctk.CTkToplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.frame = ctk.CTkFrame(self)
        self.frame_substituir = ctk.CTkFrame(self)
        self.frame.pack(pady=0, padx=0, side=ctk.TOP, fill="x")
        self.frame_substituir.pack(pady=0, padx=0, side=ctk.TOP, fill="x")

        self.title("Substituir")
        self.geometry("600x300")

        # Configurações do frame
        self.label = ctk.CTkLabel(self.frame, text="Localizar:")
        self.label.pack(padx=5,pady=20, side = ctk.LEFT)
        self.entry = ctk.CTkEntry(self.frame)
        self.entry.pack(padx=5, side = ctk.LEFT)
        self.button = ctk.CTkButton(self.frame, text="Localizar Próxima")
        self.button.pack(pady=10,side = ctk.LEFT)

        # Configurações do frame de substituir
        self.label_substituir = ctk.CTkLabel(self.frame_substituir, text="Substituir:")
        self.label_substituir.pack(padx=5,pady=20, side = ctk.LEFT)
        self.entry_substituir = ctk.CTkEntry(self.frame_substituir)
        self.entry_substituir.pack(padx=5, side = ctk.LEFT)
        self.button_subs = ctk.CTkButton(self.frame_substituir, text="Substituir")
        #self.button_subs_all = ctk.CTkButton(self.frame_substituir, text="Substituir Tudo")
        #self.button_subs_all.pack(padx=100,pady=10,side = ctk.BOTTOM)
        self.button_subs.pack(pady=10,side = ctk.LEFT)


