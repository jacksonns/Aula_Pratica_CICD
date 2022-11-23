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
    
    def test_invalid_matrix_multiplication(self, calculator):
        A = [[1,2,3],
             [4,5,6]]
        B = [[3,2,1],
             [6,5,4]]
        with pytest.raises(Exception):
            calculator.multiply_matrix(A, B)
    
    def test_invalid_matrix_multiplication(self, calculator):
        A = [[3,4],
             [2,1]]
        B = [[1,5],
             [3,7]]
        result = [[15,43],
                  [5,17]]
        assert calculator.multiply_matrix(A,B) == result