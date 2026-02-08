from Basic_Python.mathutils_py import MathUtils
import pytest

@pytest.fixture
def math_utils():
    return MathUtils()

def test_add(math_utils):
    assert math_utils.add(1, 2) == 3
    assert math_utils.add(-1, 1) == 0
    assert math_utils.add(-1, -1) == -2
    assert math_utils.add(0, 0) == 0

def test_subtract(math_utils):
    assert math_utils.subtract(5, 3) == 2
    assert math_utils.subtract(3, 5) == -2
    assert math_utils.subtract(-1, 1) == -2
    assert math_utils.subtract(1, -1) == 2
    assert math_utils.subtract(0, 0) == 0

def test_multiply(math_utils):
    assert math_utils.multiply(2, 3) == 6
    assert math_utils.multiply(-1, 5) == -5
    assert math_utils.multiply(-1, -1) == 1
    assert math_utils.multiply(0, 10) == 0
    assert math_utils.multiply(10, 0) == 0

def test_divide(math_utils):
    assert math_utils.divide(6, 2) == 3.0
    assert math_utils.divide(5, 2) == 2.5
    assert math_utils.divide(-6, 2) == -3.0
    assert math_utils.divide(6, -2) == -3.0
    assert math_utils.divide(0, 5) == 0.0
    assert math_utils.divide(5, 0) == -1.0 # Division by zero
    assert math_utils.divide(-5, 0) == -1.0 # Division by zero with negative numerator
