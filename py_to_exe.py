import os
import subprocess
import tkinter as tk
from tkinter import filedialog

# Function to convert Python script to EXE
def convert_to_exe():
    file_path = filedialog.askopenfilename(title="Select Python Script", filetypes=[("Python Files", "*.py")])
    if file_path:
        # Run pyinstaller command
        command = f'pyinstaller --onefile "{file_path}"'
        subprocess.run(command, shell=True)
        label.config(text=f"Converted: {file_path}")

# Create a simple GUI to select the Python file
app = tk.Tk()
app.title("Python to EXE Converter")

label = tk.Label(app, text="Click the button to select a Python script")
label.pack(pady=10)

convert_button = tk.Button(app, text="Select and Convert", command=convert_to_exe)
convert_button.pack(pady=10)

app.geometry("300x150")
app.mainloop()
