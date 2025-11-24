import ttkbootstrap as ttk
import tkinter as tk

class JanelaSubstituir(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.frame = ttk.Frame(self)
        self.frame_substituir = ttk.Frame(self)
        self.frame.pack(pady=0, padx=0, side=ttk.TOP, fill="x")
        self.frame_substituir.pack(pady=0, padx=0, side=ttk.TOP, fill="x")

        self.title("Substituir")
        self.geometry("600x300")

        # Configurações do frame
        self.label = ttk.Label(self.frame, text="Localizar:", relief="flat")
        self.label.pack(padx=5, pady=20, side=ttk.LEFT)
        self.entry = ttk.Entry(self.frame, bootstyle="dark")
        self.entry.pack(padx=5, side=ttk.LEFT)
        self.button = ttk.Button(self.frame, text="Localizar Próxima", bootstyle="dark")
        self.button.pack(pady=20, side=ttk.LEFT)

        # Configurações do frame de substituir
        self.label_substituir = ttk.Label(self.frame_substituir, text="Substituir:")
        self.label_substituir.pack(padx=5, pady=0, side=ttk.LEFT)
        self.entry_substituir = ttk.Entry(self.frame_substituir, bootstyle="dark")
        self.entry_substituir.pack(padx=5, side=ttk.LEFT)
        self.button_subs = ttk.Button(self.frame_substituir, text="Substituir", bootstyle="dark")
        self.button_subs.pack(pady=0, side=ttk.LEFT, padx=0)
        #self.button_subs_all = ttk.Button(self.frame_substituir, text="Substituir Tudo", bootstyle="dark")
        #self.button_subs_all.pack(padx=0, side=ttk.RIGHT)


