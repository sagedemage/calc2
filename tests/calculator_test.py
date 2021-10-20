from calculator.main import calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = calculator()
    #Act by calling the mthod to be tested
    calc.add_number()
    #Assert that the results are correct
    assert calc.result == 1

    def test_calculator_get_result():
        """Testing the Get result method of the calculator."""
        calc = calculator()
        calc.add_number(1)
        assert calc.get_result == 1

    def test_calculator_subtract():
        """Testing the subtract method of the calculator"""
        cal = calculator()
        calc.subtract_number(1)
        assert calc.get_result() == -1