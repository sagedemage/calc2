"""Import the calculator class"""
from calculator.main import Calculator


def test_calculator_result():
    """Testing calculator result is 0"""
    calc = Calculator
    assert calc.result == 0


def test_calculator_add():
    """Testing the Add function of the calculator"""
    # Arrange by instantiating the calc class
    calc = Calculator()
    # Act by calling the method to be tested
    calc.add_number(1)
    # Assert that the results are correct
    assert calc.result == 1


def test_calculator_get_result():
    """Testing the Get result method of the calculator."""
    calc = Calculator()
    calc.add_number(1)
    assert calc.get_result() == 1


def test_calculator_subtract():
    """Testing the Subtract function of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.result == -1


def test_calculator_multiply():
    """Testing the Multiply function of the calculator"""
    calc = Calculator()
    calc.multiply_number(1)
    assert calc.result == 0


def test_calculator_divide():
    """Testing the Divide function of the calculator"""
    calc = Calculator()
    calc.divide_number(1)
    # Checking if the calculator program throws ZeroDivisionError
    # calc.divide_number(0)
    assert calc.result == 0
