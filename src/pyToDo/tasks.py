import customtkinter as ctk
import json
from tkinter import BooleanVar


class NewTask(ctk.CTk):
    def __init__(self, parent=None):
        super().__init__()

        self.parent = parent

        self.geometry("800x600")
        self.title("New Task")
        self.resizable(False, False)

        for i in range(8):
            self.grid_rowconfigure(i, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Task Name
        ctk.CTkLabel(self, text="Task Name").grid(
            row=0, sticky="w", padx=20, pady=(20, 2)
        )
        self.task_name_entry = ctk.CTkEntry(self, placeholder_text="Enter Task Name")
        self.task_name_entry.grid(row=1, sticky="ew", padx=20, pady=2)

        # Description
        ctk.CTkLabel(self, text="Task Description").grid(
            row=2, sticky="w", padx=20, pady=(10, 2)
        )
        self.task_description_entry = ctk.CTkTextbox(self, height=180)
        self.task_description_entry.grid(row=3, sticky="nsew", padx=20, pady=2)

        # Due Date
        ctk.CTkLabel(self, text="Due Date").grid(
            row=4, sticky="w", padx=20, pady=(10, 2)
        )
        self.task_date_entry = ctk.CTkEntry(
            self, placeholder_text="YYYY-MM-DD or any format"
        )
        self.task_date_entry.grid(row=5, sticky="ew", padx=20, pady=2)

        # Done Checkbox
        self.isDone = BooleanVar(value=False)
        self.task_done_checkbox = ctk.CTkCheckBox(
            self, text="Mark as done immediately", variable=self.isDone
        )
        self.task_done_checkbox.grid(row=6, sticky="w", padx=20, pady=(10, 2))

        # Buttons
        btn_frame = ctk.CTkFrame(self)
        btn_frame.grid(row=7, column=0, sticky="e", padx=20, pady=(20, 20))

        ctk.CTkButton(btn_frame, text="Cancel", command=self.destroy).pack(
            side="left", padx=10
        )
        ctk.CTkButton(btn_frame, text="Add Task", command=self.add_task).pack(
            side="left", padx=10
        )

    def add_task(self):
        name = self.task_name_entry.get().strip()
        description = self.task_description_entry.get("0.0", "end").strip()
        due_date = self.task_date_entry.get().strip()
        status = "Done" if self.isDone.get() else "Pending"

        if not name:
            return

        new_task = {
            "name": name,
            "description": description,
            "due_date": due_date or "—",
            "status": status,
        }

        # Load existing tasks
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                tasks = json.load(f)
        except FileNotFoundError, json.JSONDecodeError:
            tasks = []

        # Add and save
        tasks.append(new_task)

        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)

        # refresh main app if parent passed
        if self.parent and hasattr(self.parent, "show_tasks"):
            self.parent.tasks = tasks
            self.parent.show_tasks()

        self.destroy()
