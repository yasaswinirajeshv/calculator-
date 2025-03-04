import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")

        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        input_frame.pack(pady=10)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 18), bd=5, relief=tk.FLAT, justify='right')
        input_field.grid(row=0, column=0, ipady=10)

        button_frame = tk.Frame(self)
        button_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, font=('Arial', 18), width=5, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        clear_button = tk.Button(button_frame, text='Clear', font=('Arial', 18), width=22, height=2, bg='red', fg='white',
                                 command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=4, pady=5)

    def on_button_click(self, button):
        if button == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = 'Error'
        else:
            self.expression += button
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
