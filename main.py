import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")  # Set initial size of the window

        self.current_expression = ""
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying calculations
        self.entry = tk.Entry(self.root, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('<-', 5, 0)  # Backspace button
        ]
        
        for (text, row, column) in buttons:
            color = 'orange' if text in ('/', '*', '-', '+', '=', '<-') else 'lightgray'
            button = tk.Button(self.root, text=text, font=('Arial', 18), width=5, height=2, bg=color, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

        # Make the grid expand when resizing the window
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == '=':
            try:
                # Evaluate the expression
                result = str(eval(self.current_expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.current_expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.current_expression = ""
        elif char == '<-':
            # Handle backspace
            self.current_expression = self.current_expression[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.current_expression)
        else:
            # Update the current expression
            self.current_expression += char
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.current_expression)

# Create the main window and pass it to the CalculatorApp
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
