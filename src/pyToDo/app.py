import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{1280}x{720}")
        self.title("pyToDo")
        self.resizable(False, False)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("../themes/dark.json")

app = App()
app.mainloop()