class Calculator:

    def sum(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y

    def mult(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y
    
    def factorial(self, x):
        if x == 0:
            return 1
        return x * self.factorial(x-1)
    
    def fibonacci_of(self, x):
        if x == 0 or x == 1:
            return 1
        return self.fibonacci_of(x-1) + self.fibonacci_of(x-2)

    
