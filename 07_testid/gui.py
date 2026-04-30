import tkinter as tk
from kalkulaator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("Pythoni Kalkulaator")
        self.root.geometry("300x400")

        # 1. Ekraani loomine
        self.display_label = tk.Label(
            root, text=self.calc.display, font=("Arial", 24), 
            anchor="e", bg="white", fg="black", padx=10, pady=20
        )
        self.display_label.pack(expand=True, fill="both")

        # 2. Nuppude raamistik
        button_frame = tk.Frame(root)
        button_frame.pack(expand=True, fill="both")

        # Nuppude paigutus (tekst, rida, tulp)
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('=', 3, 1), ('+', 3, 2), ('C', 3, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(
                button_frame, text=text, font=("Arial", 18),
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, sticky="nsew")

        # Muudame nupud venivaks
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char.isdigit():
            self.calc.press_number(char)
        elif char in ('+', '-', '*', '/'):
            self.calc.press_operator(char)
        elif char == '=':
            self.calc.press_equal()
        elif char == 'C':
            # Alustame puhtalt lehelt
            self.calc = Calculator()
            
        # Uuendame ekraani teksti vastavalt kalkulaatori olekule
        self.display_label.config(text=self.calc.display)

if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()