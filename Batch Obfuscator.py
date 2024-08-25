import tkinter as tk
from tkinter import filedialog, messagebox
import random


def obfuscate_content(content):
    obfuscated = []
    for char in content:
        obfuscated.append(chr(ord(char) + random.randint(1, 10)))
    return ''.join(obfuscated)

def obfuscate_file(input_path):
    try:
        with open(input_path, 'r') as file:
            content = file.read()
        
        obfuscated_content = obfuscate_content(content)
        output_path = input_path + '.obf'

        with open(output_path, 'w') as file:
            file.write(obfuscated_content)
        
        messagebox.showinfo("Success", f"File obfuscated successfully: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Batch files", "*.bat")])
    if file_path:
        obfuscate_file(file_path)

root = tk.Tk()
root.title("Batch File Obfuscator Made By King")

root.geometry("400x150")

button = tk.Button(root, text="Select Batch File to Obfuscate", command=select_file)
button.pack(pady=55)

root.mainloop()