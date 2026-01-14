import ttkbootstrap as ttk
import tkinter as tk # type: ignore


class JanelaSubstituir(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.quadro_cabeçalho = tk.Frame(self)
        self.quadro_bottom = tk.Frame(self)
        self.quadro_cabeçalho.pack(anchor= 'w', expand= False, pady=5)
        self.quadro_bottom.pack(anchor= 'w')


        self.title("Substituir")
        self.geometry("600x300") 
        self.label = ttk.Label(self.quadro_cabeçalho, text="Localizar:", relief="flat", font=("mincho", 10), style="dark", anchor="w")
        self.label.grid(row=20,column=4,padx=5, pady=0,columnspan=1,sticky="w",)

        self.entry = ttk.Entry(self.quadro_cabeçalho, bootstyle="dark")
        self.entry.grid(row=20, column=5,padx=0, pady=10,columnspan=2, sticky="w"
                        )
        self.button = ttk.Button(self.quadro_cabeçalho, text="Localizar Próxima", bootstyle="dark")
        self.button.grid(row=20, column=8,padx=5, pady=20,columnspan=2, sticky="ew")

        self.label_substituir = ttk.Label(self.quadro_cabeçalho, text="Substituir:")
        self.label_substituir.grid(row=21, column=4,padx=5, pady=0,columnspan=1,sticky="w")
        self.entry_substituir = ttk.Entry(self.quadro_cabeçalho, bootstyle="dark",font=("mincho", 10))
        self.entry_substituir.grid(row=21, column=5,padx=0, pady=0,columnspan=1, sticky="w")
        self.button_subs = ttk.Button(self.quadro_cabeçalho, text="Substituir", bootstyle="dark")
        self.button_subs.grid(row=21, column=8,padx=5, pady=0,columnspan=1, sticky="ew")

        self.checkbutton = ttk.Checkbutton(self.quadro_bottom,bootstyle='dark', text='Diferenciar minúsculas e maiúsculas')
        self.checkbutton.grid(row=22, column=6, pady=10, padx=5)
        self.checkbutton_2 = ttk.Checkbutton(self.quadro_bottom,bootstyle='dark', text='Coincidir com palavra inteira.')
        self.checkbutton_2.grid(row=24, column=6, padx=5, pady=0, sticky='ew')
