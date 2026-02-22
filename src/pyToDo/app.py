import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{1280}x{720}")
        self.title("pyToDo")
        self.resizable(False, False)

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("../themes/dark.json")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

     #1st row

        self.new_task_button = ctk.CTkButton(
            self, text="New Task"
        )
        self.new_task_button.grid(
            column=0, row=0, sticky="nw", padx=10, pady=10
        )

        self.search_entry = ctk.CTkEntry(
            self, placeholder_text="Search Task"
        )
        self.search_entry.grid(
            column=1, row=0, sticky="nsew", padx=10, pady=10
        )

        self.toggle_select_button = ctk.CTkButton(
            self, text="Select"
        )
        self.toggle_select_button.grid(
            column=2, row=0, sticky="ne", padx=10, pady=10
        )

        # 2nd row

        self.task_frame = ctk.CTkFrame(
            self
        )
        self.task_frame.grid(
            columnspan=3, row=1, sticky="nsew", padx=10, pady=(0, 10)
        )

        self.task_frame.grid_columnconfigure(0, weight=0)
        self.task_frame.grid_columnconfigure(1, weight=0)
        self.task_frame.grid_columnconfigure(2, weight=1)
        self.task_frame.grid_columnconfigure(3, weight=0)
        self.task_frame.grid_columnconfigure(4, weight=0)
        self.task_frame.grid_columnconfigure(5, weight=0)
        self.task_frame.grid_columnconfigure(6, weight=0)
        self.task_frame.grid_rowconfigure(0, weight=0)
        self.task_frame.grid_rowconfigure(1, weight=0)


        self.task_spacer1 = ctk.CTkButton(self.task_frame, text=" | ", fg_color="transparent", cursor="hand2", hover=False)
        self.task_spacer2 = ctk.CTkButton(self.task_frame, text=" | ", fg_color="transparent", cursor="hand2", hover=False)
        self.task_spacer3 = ctk.CTkButton(self.task_frame, text=" | ", fg_color="transparent", cursor="hand2", hover=False)

        # place
        self.task_spacer1.grid(row=0, column=1, sticky="ns", pady=1)
        self.task_spacer2.grid(row=0, column=3, sticky="ns", pady=1)
        self.task_spacer3.grid(row=0, column=5, sticky="ns", pady=1)

        self.task_name_button = ctk.CTkButton(
            self.task_frame, text="Name", fg_color="transparent", height=15, cursor="hand2", hover=False
        )
        self.task_name_button.grid(
            column=0, row=0, padx=4, pady=4
        )

        self.task_description_button = ctk.CTkButton(
            self.task_frame, text="Description", fg_color="transparent", height=15, cursor="hand2", hover=False
        )
        self.task_description_button.grid(
            column=2, row=0, pady=4
        )

        self.task_date_button = ctk.CTkButton(
            self.task_frame, text="Date/Until", fg_color="transparent", height=15, cursor="hand2", hover=False
        )
        self.task_date_button.grid(
            column=4, row=0, pady=4
        )

        self.task_status_button = ctk.CTkButton(
            self.task_frame, text="Status", fg_color="transparent", height=15, cursor="hand2", hover=False
        )
        self.task_status_button.grid(
            column=6, row=0,padx=4, pady=4
        )

app = App()
app.mainloop()