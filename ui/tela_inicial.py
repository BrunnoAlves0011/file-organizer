import customtkinter
from core.run import run_organizer
# from settings import exibir_relatorio, simula

class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.folder = ''

        self.input_text = customtkinter.CTkLabel(self, text="Selecione uma pasta", width=90, height=28)
        self.input_text.grid(row=0, column=0, padx=5, pady=0)

        self.input_folder = customtkinter.CTkEntry(self, width=350, height=28)
        self.input_folder.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        # self.input_folder.configure(state="disabled")

        self.select_folder = customtkinter.CTkButton(self, width=50, text="Procurar", command=self.search_folder)
        self.select_folder.grid(row=0, column=2, padx=0, pady=0, sticky="ew")

    def search_folder(self):
        self.input_folder.insert(0, '')
        self.folder = customtkinter.filedialog.askdirectory()
        self.input_folder.insert(0, str(self.folder))
        return

# Class Checkbox
class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="Exibir Relatorio")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=0, sticky="w")

        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="Simular Organizacao")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w") 

    def set_flags(self):
        self.exibir_relatorio = self.checkbox_1.get() == 1
        self.simula = self.checkbox_2.get() == 1 
        return

# Class Principal
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Titulo da guia/janela
        self.title("FileOrganizer")
        self.iconbitmap('./assets/icon/folder.bmp')

        # Tamanho da janela
        self.geometry("575x150")
        self.resizable(False, False)

        # Aparencia
        self._set_appearance_mode("dark")

        # Configuração Coluna e Linha
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Frame 1 - Input
        self.input_frame = InputFrame(self)
        self.input_frame.grid(row=0, column=0, padx=10, pady=0, sticky="w")
        self.input_frame.configure(fg_color=["gray92", "gray14"])

        # Frame 2 - Checkboxes
        self.checkbox_frame = CheckboxFrame(self)
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=0, sticky="ew")
        self.checkbox_frame.configure(fg_color=["gray92", "gray14"])

        # Botão para iniciar
        self.button = customtkinter.CTkButton(self, text="Organizar Arquivos", command=self.file_organizer)
        self.button.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="ew")

    def file_organizer(self):
        self.checkbox_frame.set_flags()
        if self.input_frame.folder != '':
            run_organizer(self.input_frame.folder, 
                          self.checkbox_frame.simula, 
                          self.checkbox_frame.exibir_relatorio)
        else:
            # Exibir mensagem de erro
            return

def tela_inicial():
    customtkinter.set_default_color_theme('./assets/theme/theme_app.json')        
    app = App()
    app.mainloop()