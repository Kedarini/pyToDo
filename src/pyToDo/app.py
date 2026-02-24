import customtkinter as ctk
from tasks import NewTask
import json

ctk.set_default_color_theme("../themes/pyToDo.json")
ctk.set_appearance_mode("Dark")


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{1280}x{720}")
        self.title("pyToDo")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        # 1st row

        self.new_task_button = ctk.CTkButton(
            self, text="New Task", command=lambda: NewTask()
        )
        self.new_task_button.grid(column=0, row=0, sticky="nw", padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(self, placeholder_text="Search Task")
        self.search_entry.grid(column=1, row=0, sticky="nsew", padx=10, pady=10)

        self.toggle_select_button = ctk.CTkButton(self, text="Select")
        self.toggle_select_button.grid(column=2, row=0, sticky="ne", padx=10, pady=10)

        # 2nd row

        # Columns

        self.task_frame = ctk.CTkFrame(self)
        self.task_frame.grid(columnspan=3, row=1, sticky="nsew", padx=10, pady=(0, 10))

        SPACER = {
            "text": "|",
            "fg_color": "transparent",
            "width": 10,
            "cursor": "sb_h_double_arrow",
            "hover": False,
        }

        self.col_weights = [20, 0, 50, 0, 15, 0, 15]
        for i, weight in enumerate(self.col_weights):
            self.task_frame.grid_columnconfigure(i, weight=weight)

        self.task_frame.grid_rowconfigure(0, weight=0)
        self.task_frame.grid_rowconfigure(1, weight=0)

        for col in [1, 3, 5]:
            self.task_spacer = ctk.CTkButton(self.task_frame, **SPACER)
            self.task_spacer.grid(row=0, column=col, sticky="ns", pady=1)

        HEADER_KWARGS = {
            "fg_color": "transparent",
            "text_color": "#eceff4",
            "anchor": "n",
            "cursor": "hand2",
            "hover": False,
        }

        self.task_name_button = ctk.CTkButton(
            self.task_frame, text="Name ▾", **HEADER_KWARGS
        )
        self.task_name_button.grid(column=0, row=0, padx=4, pady=4)

        self.task_description_button = ctk.CTkButton(
            self.task_frame, text="Description ▾", **HEADER_KWARGS
        )
        self.task_description_button.grid(column=2, row=0, pady=4)

        self.task_date_button = ctk.CTkButton(
            self.task_frame, text="Due date ▾", **HEADER_KWARGS
        )
        self.task_date_button.grid(column=4, row=0, pady=4)

        self.task_status_button = ctk.CTkButton(
            self.task_frame, text="Status", **HEADER_KWARGS
        )
        self.task_status_button.grid(column=6, row=0, padx=4, pady=4)

        self.show_tasks()

    def show_tasks(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                tasks = json.load(f)
        except FileNotFoundError, json.JSONDecodeError:
            tasks = []

        self.task_row = ctk.CTkScrollableFrame(self.task_frame)
        self.task_row.grid(columnspan=7, row=1, sticky="we")

        for i, task in enumerate(tasks, start=1):
            name = task.get("name", "—")
            desc = task.get("description", "").strip()[:80] + (
                "..." if len(task.get("description", "")) > 80 else ""
            )
            due = task.get("due_date", "—")
            status = task.get("status", "Pending")

            ctk.CTkLabel(self.task_row, text=name, anchor="center").grid(
                row=i, column=0, sticky="ew", padx=8, pady=6
            )

            ctk.CTkLabel(
                self.task_row, text=desc, anchor="center", wraplength=400
            ).grid(row=i, column=2, sticky="ew", padx=8, pady=6)

            ctk.CTkLabel(self.task_row, text=due, anchor="center").grid(
                row=i, column=4, sticky="ew", padx=8, pady=6
            )

            status_label = ctk.CTkLabel(
                self.task_row,
                text=status,
                text_color="orange" if status == "Pending" else "green",
                anchor="center",
            )
            status_label.grid(row=i, column=6, sticky="ew", padx=8, pady=6)
