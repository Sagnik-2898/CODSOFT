import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        pass

def edit_task():
    try:
        index = listbox_tasks.curselection()[0]
        current_task = listbox_tasks.get(index)
        new_task = entry_task.get()
        if current_task and new_task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, new_task)
            entry_task.delete(0, tk.END)
    except IndexError:
        pass

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and set up the widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack(side=tk.LEFT)

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack(side=tk.LEFT)

button_edit_task = tk.Button(root, text="Edit Task", command=edit_task)
button_edit_task.pack(side=tk.LEFT)

button_clear_tasks = tk.Button(root, text="Delete All Tasks", command=clear_tasks)
button_clear_tasks.pack(side=tk.LEFT)

button_save_tasks = tk.Button(root, text="Save Tasks", command=save_tasks)
button_save_tasks.pack(side=tk.LEFT)



root.mainloop()
