import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_task_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=60, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_task_button.grid(row=2, column=0, padx=10, pady=10)

        clear_all_button = tk.Button(root, text="Clear All", command=self.clear_all_tasks)
        clear_all_button.grid(row=2, column=1, padx=10, pady=10)

        self.update_task_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task to add.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks.pop(index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_all_tasks(self):
        confirmed = messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
        if confirmed:
            self.tasks.clear()
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


root = tk.Tk()
app = TodoListApp(root)

root.mainloop()
