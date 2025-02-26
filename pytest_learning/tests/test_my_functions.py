import pytest
import time
import pytest_learning.source.my_functions as my_functions


@pytest.mark.parametrize(
    "number_one, number_two, expected_result", [(1, 4, 5), (2, 3, 5)]
)
def test_add_parametrized(number_one, number_two, expected_result):
    result = my_functions.add(number_one, number_two)
    assert result == expected_result, "Addition failed"


def test_add_strings():
    result = my_functions.add("Hello", "World")
    assert result == "HelloWorld", "Addition failed"


def test_divide():
    result = my_functions.divide(4, 2)
    assert result == 2, "Division failed"


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(4, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(0.2)
    result = my_functions.divide(10, 5)
    assert result == 2


@pytest.mark.skip(reason="This feature is not yet implemented")
def test_add():
    assert my_functions.add(1, 2) == 3


@pytest.mark.xfail(reason="we know we cannot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(4, 0)
