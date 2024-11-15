import pytest

from pytest_learning.source import Rectangle


@pytest.fixture
def my_rectangle():
    return Rectangle(10, 20)


@pytest.fixture
def weired_rectangle():
    return Rectangle(5, 6)
