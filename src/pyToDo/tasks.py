import customtkinter as ctk
import json


class NewTask(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{800}x{600}")
        self.title = "New Task"
        self.resizable(False, False)

        self.row_weights = [0, 0, 0, 0, 0, 0, 0]
        for i, weight in enumerate(self.row_weights):
            self.grid_rowconfigure(i, weight=weight)

        self.task_name_label = ctk.CTkLabel(self, text="Task Name")
        self.task_name_label.grid(row=0, sticky="w", padx=10, pady=2)

        self.task_name_entry = ctk.CTkEntry(self, placeholder_text="Enter Task Name")
        self.task_name_entry.grid(row=1, sticky="w", padx=10, pady=2)

        self.task_description_label = ctk.CTkLabel(self, text="Task Description")
        self.task_description_label.grid(row=2, sticky="w", padx=10, pady=2)
        self.task_description_entry = ctk.CTkTextbox(
            self
        )
        self.task_description_entry.grid(row=3, sticky="w", padx=10, pady=2)

        self.task_date_label = ctk.CTkLabel(self, text="Due date")
        self.task_date_label.grid(row=4, sticky="w", padx=10, pady=2)
        self.task_date_entry = ctk.CTkEntry(self, placeholder_text="Enter Due Date")
        self.task_date_entry.grid(row=5, sticky="w", padx=10, pady=2)

        self.add_button = ctk.CTkButton(self, text="Add", command=self.add_task)
        self.add_button.grid(row=6, sticky="se", padx=10, pady=2)

        # json
    def add_task(self):

        name = self.task_name_entry.get().strip()
        description = self.task_description_entry.get("0.0", "end").strip()
        due_date = self.task_date_entry.get().strip()

        tasks = []

        new_task = {
            "name": name,
            "description": description,
            "due_date": due_date,
        }

        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []

        tasks.append(new_task)
        print(new_task)

        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)

        self.after(100, self.destroy)