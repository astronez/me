import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text.get(1.0, tk.END)
            file.write(content)

root = tk.Tk()
root.title("Simple Text Editor")

text = tk.Text(root, wrap="word", undo=True)
text.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()
