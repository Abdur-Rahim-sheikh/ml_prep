import pytest
from pytest_learning.source import Square


@pytest.mark.parametrize("side, expected_area", [(5, 25), (0, 0), (4, 16), (1, 1)])
def test_multiple_square_areas(side, expected_area):
    assert Square(side).area() == expected_area


@pytest.mark.parametrize("side, expected_perimeter", [(3, 12), (0, 0), (1, 4), (5, 20)])
def test_multiple_perimeters(side, expected_perimeter):
    assert Square(side).perimeter() == expected_perimeter
