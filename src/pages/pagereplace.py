import ttkbootstrap as ttk
import tkinter as tk # type: ignore


class JanelaSubstituir(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.title("Substituir")
        self.geometry("600x300") 
        self.label = ttk.Label(self, text="Localizar:", relief="flat", font=("mincho", 10), style="dark")
        self.label.grid(row=20,column=4,padx=2, pady=0,columnspan=2,sticky="ew",)

        self.entry = ttk.Entry(self, bootstyle="dark")
        self.entry.grid(row=20, column=6,padx=0, pady=30,columnspan=2, sticky="ew"
                        )
        self.button = ttk.Button(self, text="Localizar Próxima", bootstyle="dark")
        self.button.grid(row=20, column=8,padx=2, pady=20,columnspan=2, sticky="ew")
        self.label_substituir = ttk.Label(self, text="Substituir:")
        self.label_substituir.grid(row=21, column=4,padx=2, pady=0,columnspan=1,sticky="ew")
        self.entry_substituir = ttk.Entry(self, bootstyle="dark",font=("mincho", 10))
        self.entry_substituir.grid(row=21, column=6,padx=0, pady=0,columnspan=1, sticky="ew")
        self.button_subs = ttk.Button(self, text="Substituir", bootstyle="dark")
        self.button_subs.grid(row=21, column=8,padx=0, pady=0,columnspan=1, sticky="ew")
        self.button_subs_all = ttk.Button(self, text="Substituir Tudo", bootstyle="dark")
        self.button_subs_all.grid(row=21, column=10,padx=0, pady=0,columnspan=1)
        self.checkbutton = ttk.Checkbutton(self,bootstyle='dark', text='Diferenciar minúsculas e maiúsculas')
        self.checkbutton_2 = ttk.Checkbutton(self,bootstyle='dark', text='Coincidir com palavra inteira.')
        self.checkbutton_2.grid(row=24, column=4, padx=2, pady=0, sticky='ew')
        self.checkbutton.grid(row=22, column=4, pady=1, padx=2)
