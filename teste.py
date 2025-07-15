import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox, font
import os

class NotePad:
    def __init__(self):
        # Configurações do CustomTkinter
        ctk.set_appearance_mode("dark")  # ou "light"
        ctk.set_default_color_theme("blue")  # ou "green", "dark-blue"
        
        # Janela principal usando CustomTkinter
        self.root = ctk.CTk()
        self.root.title("Bloco de Notas Moderno")
        self.root.geometry("800x600")
        
        # Variáveis
        self.current_file = None
        self.is_modified = False
        
        # Criar interface
        self.create_widgets()
        self.create_menu()
        
        # Bind para detectar modificações
        self.text_area.bind('<KeyPress>', self.on_text_change)
        
    def create_widgets(self):
        # Frame principal usando CustomTkinter
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Toolbar com botões CustomTkinter
        toolbar = ctk.CTkFrame(main_frame, height=50)
        toolbar.pack(fill="x", padx=5, pady=5)
        
        # Botões da toolbar
        self.new_btn = ctk.CTkButton(toolbar, text="Novo", command=self.new_file, width=70)
        self.new_btn.pack(side="left", padx=5, pady=5)
        
        self.open_btn = ctk.CTkButton(toolbar, text="Abrir", command=self.open_file, width=70)
        self.open_btn.pack(side="left", padx=5, pady=5)
        
        self.save_btn = ctk.CTkButton(toolbar, text="Salvar", command=self.save_file, width=70)
        self.save_btn.pack(side="left", padx=5, pady=5)
        
        self.save_as_btn = ctk.CTkButton(toolbar, text="Salvar Como", command=self.save_as_file, width=90)
        self.save_as_btn.pack(side="left", padx=5, pady=5)
        
        # Separador
        separator = ctk.CTkFrame(toolbar, width=2)
        separator.pack(side="left", fill="y", padx=10, pady=5)
        
        # Controles de fonte
        self.font_var = tk.StringVar(value="Arial")
        self.font_combo = ctk.CTkComboBox(toolbar, values=["Arial", "Times New Roman", "Courier New", "Verdana"], 
                                        variable=self.font_var, command=self.change_font, width=120)
        self.font_combo.pack(side="left", padx=5, pady=5)
        
        self.size_var = tk.StringVar(value="12")
        self.size_combo = ctk.CTkComboBox(toolbar, values=["8", "10", "12", "14", "16", "18", "20", "24"], 
                                        variable=self.size_var, command=self.change_font, width=60)
        self.size_combo.pack(side="left", padx=5, pady=5)
        
        # Frame para área de texto
        text_frame = ctk.CTkFrame(main_frame)
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Área de texto usando Tkinter (pois CustomTkinter não tem Text widget robusto)
        self.text_area = tk.Text(text_frame, 
                               wrap="word", 
                               font=("Arial", 12),
                               bg="#2B2B2B",  # Cor de fundo escura
                               fg="white",    # Texto branco
                               insertbackground="white",  # Cursor branco
                               selectbackground="#1F538D",  # Seleção azul
                               relief="flat",
                               padx=10, 
                               pady=10)
        
        # Scrollbar usando CustomTkinter
        scrollbar = ctk.CTkScrollbar(text_frame, command=self.text_area.yview)
        scrollbar.pack(side="right", fill="y")
        
        self.text_area.config(yscrollcommand=scrollbar.set)
        self.text_area.pack(side="left", fill="both", expand=True)
        
        # Barra de status usando CustomTkinter
        self.status_bar = ctk.CTkLabel(main_frame, text="Pronto", anchor="w")
        self.status_bar.pack(fill="x", padx=5, pady=5)
        
    def create_menu(self):
        # Menu usando Tkinter tradicional (CustomTkinter não tem menu nativo)
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menu Arquivo
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Novo", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Abrir", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Salvar", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Salvar Como", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.quit_app, accelerator="Ctrl+Q")
        
        # Menu Editar
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Desfazer", command=lambda: self.text_area.event_generate("<<Undo>>"))
        edit_menu.add_command(label="Refazer", command=lambda: self.text_area.event_generate("<<Redo>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Cortar", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copiar", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Colar", command=lambda: self.text_area.event_generate("<<Paste>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Selecionar Tudo", command=lambda: self.text_area.tag_add("sel", "1.0", "end"))
        
        # Menu Visualizar
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Visualizar", menu=view_menu)
        view_menu.add_command(label="Tema Escuro", command=lambda: self.change_theme("dark"))
        view_menu.add_command(label="Tema Claro", command=lambda: self.change_theme("light"))
        
        # Atalhos do teclado
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-Shift-S>', lambda e: self.save_as_file())
        self.root.bind('<Control-q>', lambda e: self.quit_app())
        
    def new_file(self):
        if self.is_modified:
            if not self.ask_save_changes():
                return
        
        self.text_area.delete("1.0", tk.END)
        self.current_file = None
        self.is_modified = False
        self.update_title()
        self.status_bar.configure(text="Novo arquivo criado")
        
    def open_file(self):
        if self.is_modified:
            if not self.ask_save_changes():
                return
        
        file_path = filedialog.askopenfilename(
            title="Abrir arquivo",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert("1.0", content)
                    self.current_file = file_path
                    self.is_modified = False
                    self.update_title()
                    self.status_bar.configure(text=f"Arquivo aberto: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao abrir arquivo: {str(e)}")
                
    def save_file(self):
        if self.current_file:
            try:
                content = self.text_area.get("1.0", tk.END + "-1c")
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.is_modified = False
                self.update_title()
                self.status_bar.configure(text=f"Arquivo salvo: {os.path.basename(self.current_file)}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar arquivo: {str(e)}")
        else:
            self.save_as_file()
            
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            title="Salvar como",
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        
        if file_path:
            try:
                content = self.text_area.get("1.0", tk.END + "-1c")
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.current_file = file_path
                self.is_modified = False
                self.update_title()
                self.status_bar.configure(text=f"Arquivo salvo como: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar arquivo: {str(e)}")
                
    def change_font(self, *args):
        font_family = self.font_var.get()
        font_size = int(self.size_var.get())
        self.text_area.configure(font=(font_family, font_size))
        
    def change_theme(self, theme):
        ctk.set_appearance_mode(theme)
        if theme == "dark":
            self.text_area.configure(bg="#2B2B2B", fg="white", insertbackground="white")
        else:
            self.text_area.configure(bg="white", fg="black", insertbackground="black")
            
    def on_text_change(self, event):
        if not self.is_modified:
            self.is_modified = True
            self.update_title()
            
    def update_title(self):
        if self.current_file:
            filename = os.path.basename(self.current_file)
            title = f"{'*' if self.is_modified else ''}{filename} - Bloco de Notas Moderno"
        else:
            title = f"{'*' if self.is_modified else ''}Sem título - Bloco de Notas Moderno"
        self.root.title(title)
        
    def ask_save_changes(self):
        if self.is_modified:
            result = messagebox.askyesnocancel("Salvar alterações", 
                                             "Deseja salvar as alterações antes de continuar?")
            if result is True:
                self.save_file()
                return True
            elif result is False:
                return True
            else:
                return False
        return True
        
    def quit_app(self):
        if self.ask_save_changes():
            self.root.destroy()
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = NotePad()
    app.run()