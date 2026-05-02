from calculator.config import CONFIG_FILE
from canvas import app, on_closing, on_state_change


if __name__ == "__main__":
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.bind("<Configure>", on_state_change)
    app.mainloop()