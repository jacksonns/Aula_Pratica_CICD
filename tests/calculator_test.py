import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    calculator = Calculator()
    return calculator

class TestCalculator:

    def test_sum(self, calculator):
        assert calculator.sum(2,2) == 4
    
    def test_subtract(self, calculator):
        assert calculator.subtract(2,2) == 0

    def test_mult(self, calculator):
        assert calculator.mult(3,2) == 6

    def test_div(self, calculator):
        assert calculator.div(2,2) == 1
    
    def test_factorial(self, calculator):
        assert calculator.factorial(5) == 120
    
    def test_factorial_of_0(self, calculator):
        assert calculator.factorial(0) == 1
    
    def test_first_fibonacci_numbers(self, calculator):
        assert calculator.fibonacci_of(0) == 1
        assert calculator.fibonacci_of(1) == 1
    
    def test_fibonacci(self,calculator):
        assert calculator.fibonacci_of(5) == 8
        assert calculator.fibonacci_of(7) == 21
