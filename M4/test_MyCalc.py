import pytest
from MyCalc import MyCalc

# rk868 16/10/2023: my_calc_instance is the pytest fixture that will create an instance of MyCalc class for each test case and pass it as an argument to the test case
@pytest.fixture
def my_calc_instance():
    return MyCalc()

# rk868 16/10/2023: Test cases for number-add-number operation using parametrize decorator to run the same test case with different inputs
#  It verifies that the calc function correctly calculates the sum and compares it to the expected result.
# The test case will pass if the actual output is equal to the expected output and fail otherwise.
@pytest.mark.parametrize("a, b, expected", [(11, 22, 33), (0, 0, 0), (-100, 100, 0), (-55.5, 55.5, 0)])
def test_add(my_calc_instance, a, b, expected):
    result = my_calc_instance.calc(a, b, "+")
    assert result == expected

# rk868 16/10/2023: Test cases for ans-add-number operation using parametrize decorator to run the same test case with different inputs
#  It sets the value of the "ans" attribute of the MyCalc instance and ensures that the calc function correctly uses it to calculate the sum.
#  The test case will pass if the actual output is equal to the expected output and fail otherwise.
@pytest.mark.parametrize("ans, b, expected", [(22, 33, 55), (0, 0, 0), (-10000, 10000, 0), (-11.1, 11.1, 0)])
def test_ans_add(my_calc_instance, ans, b, expected):
    my_calc_instance.ans = ans
    result = my_calc_instance.calc("ans", b, "+")
    assert result == expected

# rk868 16/10/2023: Test cases for number-subtract-number operation using parametrize decorator to run the same test case with different inputs
#  It verifies that the calc function correctly calculates the difference and compares it to the expected result.
#  The test case will pass if the actual output is equal to the expected output and fail otherwise.
@pytest.mark.parametrize("a, b, expected", [(22, 11, 11), (0, 0, 0), (-100, 100, -200), (-55.5, 55.5, -111)])
def test_sub(my_calc_instance, a, b, expected):
    result = my_calc_instance.calc(a, b, "-")
    assert result == expected

# rk868 16/10/2023: Test cases for ans-subtract-number operation using parametrize decorator to run the same test case with different inputs
#  It sets the value of the "ans" attribute of the MyCalc instance and ensures that the calc function correctly uses it to calculate the difference.
#  The test case will pass if the actual output is equal to the expected output and fail otherwise.
@pytest.mark.parametrize("ans, b, expected", [(23, 11, 12), (0, 0, 0), (-100, 100, -200), (-23.4, 45.6, -69.0)])
def test_ans_sub(my_calc_instance, ans, b, expected):
    my_calc_instance.ans = ans
    result = my_calc_instance.calc("ans", b, "-")
    assert result == expected

# rk868 16/10/2023: Test cases for number-multiply-number operation using parametrize decorator to run the same test case with different inputs
#  It verifies that the calc function correctly calculates the product and compares it to the expected result.
#  The test case will pass if the actual output is equal to the expected output and fail otherwise.
@pytest.mark.parametrize("a, b, expected", [(32, 2, 64), (0, 0, 0), (-100, 100, -10000), (-2.5, 2.5, -6.25)])
def test_mult(my_calc_instance, a, b, expected):
    result = my_calc_instance.calc(a, b, "*")
    assert result == expected

# rk868 16/10/2023: Test cases for ans-multiply-number operation using parametrize decorator to run the same test case with different inputs
#  It sets the value of the "ans" attribute of the MyCalc instance and ensures that the calc function correctly uses it to calculate the product.
#  The test case will pass if the actual output is equal to the expected output and fail otherwise.
@pytest.mark.parametrize("ans, b, expected", [(15, 2, 30), (0, 0, 0), (-100, 100, -10000), (-1.2, 1.2, -1.44)])
def test_ans_mult(my_calc_instance, ans, b, expected):
    my_calc_instance.ans = ans
    result = my_calc_instance.calc("ans", b, "*")
    assert result == expected

# rk868 16/10/2023: Test cases for number-divide-number operation using parametrize decorator to run the same test case with different inputs
#  It verifies that the calc function correctly calculates the quotient and compares it to the expected result.
#  The test case will pass if the actual output is equal to the expected output and fail otherwise.
@pytest.mark.parametrize("a, b, expected", [(64, 4, 16), (-100, 100, -1), (-1.1, 1.1, -1.0)])
def test_div(my_calc_instance, a, b, expected):
    result = my_calc_instance.calc(a, b, "/")
    assert result == expected

# rk868 16/10/2023: Confirm that the calc function raises a ZeroDivisionError exception when the divisor is zero.
def test_div_zero(my_calc_instance):
    with pytest.raises(ZeroDivisionError):
        my_calc_instance.calc(1, 0, "/")

# rk868 16/10/2023: Test cases for ans-divide-number operation using parametrize decorator to run the same test case with different inputs
#  It sets the value of the "ans" attribute of the MyCalc instance and ensures that the calc function correctly uses it to calculate the quotient.
#  The test case will pass if the actual output is equal to the expected output and fail otherwise.
@pytest.mark.parametrize("ans, b, expected", [(32, 2, 16), (-100, 100, -1), (-2.5, 2.5, -1.0)])
def test_ans_div(my_calc_instance, ans, b, expected):
    my_calc_instance.ans = ans
    result = my_calc_instance.calc("ans", b, "/")
    assert result == expected

# rk868 16/10/2023: Confirm that the calc function raises a ZeroDivisionError exception when the denominator is zero.
def test_ans_div_zero(my_calc_instance):
    my_calc_instance.ans = 1
    with pytest.raises(ZeroDivisionError):
        my_calc_instance.calc("ans", 0, "/")