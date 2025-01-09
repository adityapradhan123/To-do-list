import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("800x400")
root.configure(bg="#97cba9")

# Global variable to track task numbers
task_number = 1

# Lists to store tasks
todo_tasks = []
in_progress_tasks = []
completed_tasks = []
all_tasks_history = []  # New list to store all tasks history

def addTask():
    global task_number
    task = entry.get().strip()
    if task:
        task_entry = f"{task_number}. [TODO] {task}"
        todo_tasks.append(task_entry)
        all_tasks_history.append(task_entry)  # Add task to history
        updateListBoxes()
        task_number += 1
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def deleteTask():
    try:
        idx = listbox_todo.curselection()[0]
        if idx < len(todo_tasks):
            todo_tasks.pop(idx)
        elif idx < len(todo_tasks) + len(in_progress_tasks):
            in_progress_tasks.pop(idx - len(todo_tasks))
        updateListBoxes()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def markInProgress():
    try:
        idx = listbox_todo.curselection()[0]
        if idx < len(todo_tasks):
            task = todo_tasks.pop(idx)
            in_progress_tasks.append(task.replace("[TODO]", "[IN PROGRESS]"))
        updateListBoxes()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as in progress.")

def markCompleted():
    try:
        idx = listbox_in_progress.curselection()[0]
        if idx < len(in_progress_tasks):
            task = in_progress_tasks.pop(idx)
            completed_tasks.append(task.replace("[IN PROGRESS]", "[COMPLETED]"))
        updateListBoxes()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

def updateListBoxes():
    listbox_todo.delete(0, tk.END)
    for task in todo_tasks:
        listbox_todo.insert(tk.END, task)

    listbox_in_progress.delete(0, tk.END)
    for task in in_progress_tasks:
        listbox_in_progress.insert(tk.END, task)

    listbox_completed.delete(0, tk.END)
    for task in completed_tasks:
        listbox_completed.insert(tk.END, task)

def displayAllTasks():
    all_tasks_window = tk.Toplevel(root)
    all_tasks_window.title("All Tasks History")
    all_tasks_window.geometry("600x400")
    all_tasks_window.configure(bg="#000000")
    
    history_listbox = tk.Listbox(all_tasks_window, width=80, height=20, font=listboxFont, selectbackground="#8e8d8a")
    history_listbox.pack(padx=10, pady=10)
    
    for task in all_tasks_history:
        history_listbox.insert(tk.END, task)

titleFont = ("Arial", 20, "bold")
buttonFont = ("Arial", 12)
entryFont = ("Arial", 14)
listboxFont = ("Arial", 12)
labelFont = ("Arial", 14, "bold")

title = tk.Label(root, text="To-Do List Application", bg="#f0e5d8", fg="#4b3832", font=titleFont)
title.pack(pady=10)

entryFrame = tk.Frame(root, bg="#f0e5d8")
entryFrame.pack(pady=5)

entryLabel = tk.Label(entryFrame, text="Enter Task:", bg="#f0e5d8", fg="#4b3832", font=buttonFont)
entryLabel.grid(row=0, column=0, padx=10)

entry = tk.Entry(entryFrame, width=30, font=entryFont)
entry.grid(row=0, column=1, padx=10)

buttonFrame = tk.Frame(root, bg="#97cba9")
buttonFrame.pack(pady=10)

addButton = tk.Button(buttonFrame, text="Add Task", bg="#8e8d8a", fg="#ffffff", font=buttonFont, command=addTask)
addButton.grid(row=0, column=0, padx=5, pady=5)

deleteButton = tk.Button(buttonFrame, text="Delete Task", bg="#e98074", fg="#ffffff", font=buttonFont, command=deleteTask)
deleteButton.grid(row=0, column=1, padx=5, pady=5)

progressButton = tk.Button(buttonFrame, text="In Progress", bg="#f39c12", fg="#ffffff", font=buttonFont, command=markInProgress)
progressButton.grid(row=0, column=2, padx=5, pady=5)

completeButton = tk.Button(buttonFrame, text="Completed Task", bg="#2ecc71", fg="#ffffff", font=buttonFont, command=markCompleted)
completeButton.grid(row=0, column=3, padx=5, pady=5)

displayAllButton = tk.Button(buttonFrame, text="Display All Tasks", bg="#6c5b7b", fg="#ffffff", font=buttonFont, command=displayAllTasks)
displayAllButton.grid(row=0, column=4, padx=5, pady=5)

exitButton = tk.Button(buttonFrame, text="Exit", bg="#d8c3a5", fg="#ffffff", font=buttonFont, command=root.quit)
exitButton.grid(row=0, column=5, padx=5, pady=5)

listboxFrame = tk.Frame(root, bg="#668ba4")
listboxFrame.pack(pady=10, padx=10, fill=tk.X)

todoLabel = tk.Label(listboxFrame, text="To Do", bg="#f0e5d8", fg="#4b3832", font=labelFont)
todoLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")

progressLabel = tk.Label(listboxFrame, text="In Progress", bg="#f0e5d8", fg="#4b3832", font=labelFont)
progressLabel.grid(row=0, column=1, padx=5, pady=5, sticky="w")

completedLabel = tk.Label(listboxFrame, text="Completed", bg="#f0e5d8", fg="#4b3832", font=labelFont)
completedLabel.grid(row=0, column=2, padx=5, pady=5, sticky="w")

listbox_todo = tk.Listbox(listboxFrame, width=60, height=10, font=listboxFont, selectbackground="#e98074")
listbox_todo.grid(row=1, column=0, padx=10, pady=10)

listbox_in_progress = tk.Listbox(listboxFrame, width=60, height=10, font=listboxFont, selectbackground="#f39c12")
listbox_in_progress.grid(row=1, column=1, padx=10, pady=10)

listbox_completed = tk.Listbox(listboxFrame, width=60, height=10, font=listboxFont, selectbackground="#2ecc71")
listbox_completed.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()
