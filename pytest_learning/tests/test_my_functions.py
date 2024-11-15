import pytest

import pytest_learning.source.my_functions as my_functions


@pytest.mark.parametrize(
    "number_one, number_two, expected_result", [(1, 4, 5), (2, 3, 5)]
)
def test_add_parametrized(number_one, number_two, expected_result):
    result = my_functions.add(number_one, number_two)
    assert result == expected_result, "Addition failed"


def test_divide():
    result = my_functions.divide(4, 2)
    assert result == 2, "Division failed"


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(4, 0)
