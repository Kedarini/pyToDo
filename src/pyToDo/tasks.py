import customtkinter as ctk
import json


class NewTask(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{400}x{300}")
        self.title = "New Task"
        self.resizable(False, False)

        self.row_weights = [0, 0, 0, 0, 0, 0]
        for i, weight in enumerate(self.row_weights):
            self.grid_rowconfigure(i, weight=weight)

        self.task_name_label = ctk.CTkLabel(self, text="Task Name")
        self.task_name_label.grid(row=0, sticky="w", padx=10, pady=2)

        self.task_name_entry = ctk.CTkEntry(self, placeholder_text="Enter Task Name")
        self.task_name_entry.grid(row=1, sticky="w", padx=10, pady=2)

        self.task_description_label = ctk.CTkLabel(self, text="Task Description")
        self.task_description_label.grid(row=2, sticky="w", padx=10, pady=2)
        self.task_description_entry = ctk.CTkEntry(
            self, placeholder_text="Enter Task Description"
        )
        self.task_description_entry.grid(row=3, sticky="w", padx=10, pady=2)

        self.task_date_label = ctk.CTkLabel(self, text="Due date")
        self.task_date_label.grid(row=4, sticky="w", padx=10, pady=2)
        self.task_date_entry = ctk.CTkEntry(self, placeholder_text="Enter Due Date")
        self.task_date_entry.grid(row=5, sticky="w", padx=10, pady=2)


class Tasks:
    def __init__(self):

        self.tasks = []
