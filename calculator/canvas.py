import tkinter as tk
import json
import os


def create_app():
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - 500) // 2
    y = (screen_height - 400) // 2

    root.geometry(f"500x400+{x}+{y}")
    root.title("Calculator")

    return root

app = create_app()