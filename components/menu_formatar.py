import tkinter as tk

class MenuFormatar(tk.Menu):
    def __init__(self, master=None):      
        super().__init__(master, tearoff=0,bg='white',activebackground="lightblue",activeforeground="black")
        self.add_cascade(label='Formatar')
        self.add_command(label='Fonte...')
        self.add_command(label='Codificar')
   