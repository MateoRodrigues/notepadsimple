import ttkbootstrap as ttk
import tkinter as tk


class AutoHideScrollbar(ttk.Scrollbar):
    def set(self, first, last):
        self._first = float(first)
        self._last = float(last)
        super().set(first, last)
        self.after(0, self._update_visibility)

    def _update_visibility(self):
        # Se o tkinter ainda está renderizando, evite conflitos
        if self._first <= 0.0 and self._last >= 1.0:
            if self.winfo_ismapped():
                self.pack_forget()
        else:
            if not self.winfo_ismapped():
                self.pack(side=tk.RIGHT, fill="y")
