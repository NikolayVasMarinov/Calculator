import tkinter as tk
from buttons import BASIC_BUTTONS, BASIC_MODE_COLUMNS, BASIC_MODE_ROWS
from canvas import app
from logic import Calculator

calculator = Calculator()


def render_calculator_screen():
    tk.Label(app, text='').grid(
        row=0, column=0,
        columnspan=4, sticky="nsew",
        ipadx=0, ipady=30
    )

    for button in BASIC_BUTTONS:
        tk.Button(
            app, text=button["text"],
            command= lambda text = button["text"]: Calculator.process_button(calculator, text)

        ).grid(
            row= button["row"], column= button["column"],
            sticky="nsew", ipadx=30, ipady=15
        )

    for row in range(BASIC_MODE_ROWS):
        app.rowconfigure(row, weight=1)

    for column in range(BASIC_MODE_COLUMNS):
        app.columnconfigure(column, weight = 1)