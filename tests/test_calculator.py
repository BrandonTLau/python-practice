import pytest
from calculator import add, subtract, multiply, divide

def test_add_positive_and_negative():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10
    assert add(0, 5.5) == 5.5

def test_subtract_values():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(-5, -5) == 0
    assert subtract(5.5, 2.0) == 3.5

def test_multiply_values():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(5, 0) == 0
    assert multiply(-2, -2) == 4

def test_divide_values():
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        divide(10, 0)
