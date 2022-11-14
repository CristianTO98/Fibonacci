import pytest

from mainFibo import fibonacci_3



def test_fibonacci_1_is_1():
    assert fibonacci_3(1) == 1

def test_fibonacci_9_is_34():
    assert fibonacci_3(9) == 34

def test_fibonacci_Negative():
    with pytest.raises(ValueError):
        fibonacci_3(-10)


