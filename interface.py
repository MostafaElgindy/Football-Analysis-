import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def is_video_file(file_path):
    valid_extensions = (".mp4", ".avi", ".mkv", ".mov", ".flv")
    return file_path.lower().endswith(valid_extensions)

def open_file_explorer():
    file_path = filedialog.askopenfilename(title="Select vedio", filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.mov *.flv")])
    if file_path:
        if is_video_file(file_path):
            messagebox.showinfo("success", f"Selected file: {os.path.basename(file_path)}")
            run_python_script(file_path)
        else:
            messagebox.showerror("Error", "Check the file type and try again.")

def run_python_script(file_path):
    try:
        python_script = "main.py"  
        subprocess.run(["python", python_script, file_path], check=True)
        messagebox.showinfo("Done", "File processed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"{e}")

root = tk.Tk()
root.title("Application")
root.geometry("300x150")

open_button = tk.Button(root, text="Select Vedio", command=open_file_explorer, width=20, height=2, bg="blue", fg="white")
open_button.pack(pady=30)

root.mainloop()
