class calculator:
    def __init__(self,add, subtract, multiply, divide):
        self.add = add
        self.subtract = subtract
        self.multiply = multiply
        self.divide = divide
        
        
    def add(a,b):
        return a + b
    
    def subtract(a,b):
        return a - b
    
    def multiply(a,b):
        return a * b
    
    def divide(a,b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
    def calculate(self):
        print(self.add(5,4))
        print(self.subtract(5,4))
        print(self.multiply(5,4))
        print(self.divide(5,4))

calc = calculator(calculator.add, calculator.subtract, calculator.multiply, calculator.divide)

calc.calculate()

        
    
        
        

        


