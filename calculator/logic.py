import tkinter as tk
from canvas import app


class Calculator:
    def __init__(self):
        self.equation = []

        self.numbers = [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
        ]

        self.operations = [
            "+",
            "-",
            "×",
            "÷",
        ]

        self.actions = {
            "C": self.clear_equation,
            "=": self.solve_equation,
            "⌫": self.remove_from_equation,
            ".": self.add_dot,
            "(": self.add_open_parenthesis,
            ")": self.add_close_parenthesis
        }

    def process_button(self, symbol):
        if symbol in self.numbers:
            self.add_number_to_equation(symbol)

        if symbol in self.operations:
            self.add_operation_to_equation(symbol)


        if symbol in self.actions:
            self.process_action(symbol)

        self.display_equation()

    def process_action(self, symbol):
        if symbol in self.actions:
            self.actions[symbol]()

    def add_dot(self):
        ...

    def add_open_parenthesis(self):
        ...

    def add_close_parenthesis(self):
        ...

    def add_number_to_equation(self, symbol):
        self.equation.append(symbol)

    def add_operation_to_equation(self, symbol):
        if self.equation:
            if self.equation[-1] not in self.operations:
                self.equation.append(symbol)

            else:
                self.equation.pop()
                self.equation.append(symbol)

        else:
            self.equation.append("0")
            self.equation.append(symbol)


    def remove_from_equation(self):
        if self.equation:
            self.equation.pop()

    def clear_equation(self):
        self.equation.clear()

    def solve_equation(self):
        ...

    def display_equation(self):
        tk.Label(app, text="".join(self.equation)).grid(
            row=0, column=0,
            columnspan=4, sticky="nsew",
            ipadx=0, ipady=30
        )