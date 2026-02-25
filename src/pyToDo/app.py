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

        self.checkboxes = []
        self.selected_tasks = {}

        # 1st row

        self.new_task_button = ctk.CTkButton(
            self, text="New Task", command=lambda: NewTask(self)
        )
        self.new_task_button.grid(column=0, row=0, sticky="nw", padx=10, pady=10)

        self.search_entry = ctk.CTkEntry(self, placeholder_text="Search Task")
        self.search_entry.grid(column=1, row=0, sticky="nsew", padx=10, pady=10)

        self.toggle_select_button = ctk.CTkButton(
            self, text="Select", command=lambda: self.select_tasks()
        )
        self.toggle_select_button.grid(column=2, row=0, sticky="ne", padx=10, pady=10)

        # 2nd row

        # Columns

        self.task_frame = ctk.CTkFrame(self, height=1000)
        self.task_frame.grid(columnspan=3, row=1, sticky="nsew", padx=10, pady=(0, 10))

        self.SPACER = {
            "text": "|",
            "fg_color": "transparent",
            "width": 10,
            "cursor": "sb_h_double_arrow",
            "hover": False,
        }

        self.col_weights = [20, 0, 50, 0, 15, 0, 15]
        self.col_weights2 = [30, 0, 30, 0, 30, 0, 30]
        for i, weight in enumerate(self.col_weights):
            self.task_frame.grid_columnconfigure(i, weight=weight)

        self.task_frame.grid_rowconfigure(0, weight=0)
        self.task_frame.grid_rowconfigure(1, weight=1)
        self.task_row = ctk.CTkScrollableFrame(self.task_frame)

        for col in [1, 3, 5]:
            self.task_spacer = ctk.CTkButton(self.task_frame, **self.SPACER)
            self.task_spacer.grid(row=0, column=col, sticky="ns", pady=1)

        self.HEADER_KWARGS = {
            "fg_color": "transparent",
            "text_color": "#eceff4",
            "anchor": "n",
            "cursor": "hand2",
            "hover": False,
        }

        self.task_name_button = ctk.CTkButton(
            self.task_frame, text="Name ▾", **self.HEADER_KWARGS
        )
        self.task_name_button.grid(column=0, row=0, padx=4, pady=4)

        self.task_description_button = ctk.CTkButton(
            self.task_frame, text="Description ▾", **self.HEADER_KWARGS
        )
        self.task_description_button.grid(column=2, row=0, pady=4)

        self.task_date_button = ctk.CTkButton(
            self.task_frame, text="Due date ▾", **self.HEADER_KWARGS
        )
        self.task_date_button.grid(column=4, row=0, pady=4)

        self.task_status_button = ctk.CTkButton(
            self.task_frame, text="Status", **self.HEADER_KWARGS
        )
        self.task_status_button.grid(column=6, row=0, padx=4, pady=4)

        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
        except FileNotFoundError, json.JSONDecodeError:
            self.tasks = []

        self.show_tasks()

    def show_tasks(self):
        self.task_row.grid(columnspan=7, row=1, sticky="nsew", padx=5, pady=(0, 5))

        for i, weight in enumerate(self.col_weights):
            self.task_row.grid_columnconfigure(i, weight=weight)

        for i, task in enumerate(self.tasks, start=1):
            name = task.get("name", "—")
            desc = task.get("description", "").strip()[:80] + (
                "..." if len(task.get("description", "")) > 80 else ""
            )
            due = task.get("due_date", "—")
            status = task.get("status", "Pending")

            ctk.CTkLabel(self.task_row, text=name, anchor="n").grid(
                row=i, column=0, padx=4, pady=4
            )

            ctk.CTkLabel(self.task_row, text=desc, anchor="n").grid(
                row=i, column=2, pady=4
            )

            ctk.CTkLabel(self.task_row, text=due, anchor="n").grid(
                row=i, column=4, pady=4
            )

            status_label = ctk.CTkLabel(
                self.task_row,
                text=status,
                text_color="orange" if status == "Pending" else "green",
                anchor="n",
            )
            status_label.grid(row=i, column=6, padx=4, pady=4)

            for col in [1, 3, 5]:
                self.task_spacer = ctk.CTkButton(self.task_row, **self.SPACER)
                self.task_spacer.grid(row=i, column=col, sticky="ns", pady=1)

    def select_tasks(self):
        if hasattr(self, "checkboxes") and self.checkboxes:
            for cb in self.checkboxes:
                cb.destroy()
            self.toggle_select_button.configure(
                text="Select", command=self.remove_tasks
            )
            self.search_entry.grid()
            self.remove_selected_button.grid_remove()
            self.show_tasks()
            return

        self.search_entry.grid_remove()

        self.remove_selected_button = ctk.CTkButton(
            self, text="Remove", fg_color="#ff6961"
        )
        self.remove_selected_button.grid(column=1, row=0, sticky="e", padx=4, pady=4)

        for idx, task in enumerate(self.tasks, start=1):
            var = ctk.BooleanVar(value=False)
            checkbox = ctk.CTkCheckBox(
                self.task_row, text="", variable=var, width=20, height=20
            )
            checkbox.grid(row=idx, column=0, sticky="w", padx=(10, 4), pady=6)

            self.checkboxes.append(checkbox)
            self.selected_tasks[idx] = var

        self.toggle_select_button.configure(text="Done")

    def remove_tasks(self):
        if not self.checkboxes:
            return

        indices_to_remove = []
        for row_idx, var in self.selected_tasks.items():
            if var.get():
                indices_to_remove.append(row_idx - 1)

        if not indices_to_remove:
            return

        indices_to_remove.sort(reverse=True)

        # Remove tasks
        for idx in indices_to_remove:
            del self.tasks[idx]

        try:
            with open("tasks.json", "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving tasks.json: {e}")

        for cb in self.checkboxes:
            cb.destroy()
        self.checkboxes.clear()
        self.selected_tasks.clear()

        self.toggle_select_button.configure(text="Select")
        self.search_entry.grid()
        self.remove_selected_button.grid_remove()

        # Refresh the list
        self.show_tasks()
