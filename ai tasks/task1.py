class Calculator:
    def __init__(self):
        self.Operations={
            "+":self.add,
            "-":self.substract,
            "*":self.multiply,
            "/":self.division
        }
    def add(self,a,b):
        return a+b
    def substract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def division(self,a,b):
        if b!=0:
            return a/b
        else:
            raise ValueError("Cannot divide by zero!")
    def calculate(self,operator,a,b):
        if operator in self.Operations:
            return self.Operations[operator](a, b)
        else:
            raise ValueError(f"Operation {operator} not supported.")
    def add_operation(self, operator, function):
        self.Operations[operator] = function
    def list_operations(self):
        return list(self.operations.keys())
cal1 = Calculator()
print(cal1.calculate('+',18, 2)) 
print(cal1.calculate('-',18, 2))  
print(cal1.calculate('*',18 ,2))  
print(cal1.calculate('/',18,2))  
