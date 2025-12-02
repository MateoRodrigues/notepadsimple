import ttkbootstrap as tb
import tkinter as tk


class AutoHideScrollbar(tb.ttk.Scrollbar):
    def set(self, low, high):
        if float(low) <= 0 and float(high) >= 1:
            self.pack_forget()
        else:
            # Conteúdo não cabe → mostrar scrollbar
            # Só mostra se ainda não estiver visível
            if not self.winfo_ismapped():
                self.pack(side=tk.RIGHT, fill="y")

        super().set()
