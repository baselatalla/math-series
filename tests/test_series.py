from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'

# testing fibonacci function 
def test_fibonacci_zero():
    expected = 0
    actual = fibonacci(0)
    assert expected == actual

def test_fibonacci_three():
    expected = 2
    actual = fibonacci(3)
    assert expected == actual

def test_fibonacci_seven():
    expected = 13
    actual = fibonacci(7)
    assert expected == actual

def test_fibonacci_nine():
    expected = 34
    actual = fibonacci(9)
    assert expected == actual


# testing lucas function 


def test_lucas_zero():
    expected = 2
    actual = lucas(0)
    assert expected == actual

def test_lucas_three():
    expected = 4
    actual = lucas(3)
    assert expected == actual

def test_lucas_seven():
    expected = 29
    actual = lucas(7)
    assert expected == actual

def test_lucas_nine():
    expected = 76
    actual = lucas(9)
    assert expected == actual




# testing sum_series function 

def test_sum_series_zero_fibonacci():
    expected = 0
    actual = sum_series(0)
    assert expected == actual

def test_sum_series_three_fibonacci():
    expected = 2
    actual = sum_series(3,0,1)
    assert expected == actual

def test_sum_series_seven_fibonacci():
    expected = 13
    actual = sum_series(7)
    assert expected == actual

def test_sum_series_nine_fibonacci():
    expected = 34
    actual = sum_series(9,0,1)
    assert expected == actual

def test_sum_series_seven_lucas():
    expected = 29
    actual = sum_series(7,2,1)
    assert expected == actual

def test_sum_series_nine_lucas():
    expected = 76
    actual = sum_series(9,2,1)
    assert expected == actual

def test_sum_series_other0():
    expected = 23
    actual = sum_series(4,4,5)
    assert expected == actual

def test_sum_series_other1():
    expected = 14
    actual = sum_series(3,4,5)
    assert expected == actual

def test_sum_series_other3():
    expected = 32
    actual = sum_series(4,7,6)
    assert expected == actual

def test_sum_series_other4():
    expected = 19
    actual = sum_series(3,7,6)
    assert expected == actual