import ttkbootstrap as ttk

class JanelaSubstituir(ttk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.frame = ttk.Frame(self)
        self.frame_substituir = ttk.Frame(self)
        self.frame.pack(pady=0, padx=0, side=ttk.TOP, fill="x")
        self.frame_substituir.pack(pady=0, padx=0, side=ttk.TOP, fill="x")

        self.title("Substituir")
        self.geometry("600x300")

        # Configurações do frame
        self.label = ttk.Label(self.frame, text="Localizar:")
        self.label.pack(padx=5, pady=20, side=ttk.LEFT)
        self.entry = ttk.Entry(self.frame)
        self.entry.pack(padx=5, side=ttk.LEFT)
        self.button = ttk.Button(self.frame, text="Localizar Próxima", bootstyle="primary")
        self.button.pack(pady=20, side=ttk.LEFT)

        # Configurações do frame de substituir
        self.label_substituir = ttk.Label(self.frame_substituir, text="Substituir:")
        self.label_substituir.pack(padx=5, pady=20, side=ttk.LEFT)
        self.entry_substituir = ttk.Entry(self.frame_substituir)
        self.entry_substituir.pack(padx=5, side=ttk.LEFT)
        self.button_subs = ttk.Button(self.frame_substituir, text="Substituir", bootstyle="info")
        self.button_subs_all = ttk.Button(self.frame_substituir, text="Substituir Tudo", bootstyle="success")
        self.button_subs_all.pack(padx=100, side=ttk.RIGHT)
        self.button_subs.pack(pady=0, side=ttk.LEFT)


