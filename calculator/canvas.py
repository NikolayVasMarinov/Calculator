import tkinter as tk
from config import save_geometry, load_geometry, load_state, save_state

last_state = {"geometry": load_geometry(), "state": load_state()}

def create_app():
    root = tk.Tk()

    geometry = load_geometry()
    state = load_state()

    root.state(state)

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

def on_state_change(event):
    state = app.state()

    if state == "iconic":
        return

    if state != "zoomed":
        last_state["geometry"] = app.geometry()
    last_state["state"] = state

def on_closing():
    save_geometry(last_state["geometry"])
    save_state(last_state["state"])
    app.destroy()

app = create_app()