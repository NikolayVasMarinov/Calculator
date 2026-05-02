from calculator.config import CONFIG_FILE
from canvas import app, on_closing


if __name__ == "__main__":
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()