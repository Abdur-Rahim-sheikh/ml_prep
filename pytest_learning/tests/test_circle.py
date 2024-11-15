from pytest_learning.source import Circle
import math

import logging

logger = logging.getLogger(__name__)


class TestCircle:

    def setup_method(self, method):
        self.circle = Circle(10)
        logger.info(f"setting up {method}")

    def teardown_method(self, method):
        del self.circle
        logger.info(f"tearing down {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
