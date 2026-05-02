import tkinter as tk
import json
import os
from config import save_geometry, load_geometry


def create_app():
    root = tk.Tk()

    geometry = load_geometry()

    if "+" in geometry:
        root.geometry(geometry)

    else:
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width - 500) // 2
        y = (screen_height - 400) // 2

        root.geometry(f"{geometry}+{x}+{y}")

    root.title("Calculator")

    return root

def on_closing():
    save_geometry(app.geometry())
    app.destroy()

app = create_app()