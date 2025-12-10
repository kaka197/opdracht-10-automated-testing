import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(10, -5) == 15
    assert calculator.subtract(0, 0) == 0

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 5) == -5
    assert calculator.multiply(0, 10) == 0

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(0, 1) == 0
    
    # Test division by zero
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
