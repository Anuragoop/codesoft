import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")

        self.tasks = []

        # Entry field
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        # Add button
        self.add_button = tk.Button(root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack()

        # Task list
        self.task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Buttons
        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_complete(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            if not task.endswith("✔️"):
                self.tasks[index] = task + " ✔️"
                self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark complete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
