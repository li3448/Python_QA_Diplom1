from parameterized import parameterized
import unittest
from praktikum.bun import Bun


class TestBunParameterized(unittest.TestCase):
    @parameterized.expand([
        ("Булочка", 50.0),
        ("Черный хлеб", 70.0),
        ("Безглютеновая булочка", 100.0),
    ])
    def test_bun_parameters(self, name, price):
        bun = Bun(name, price)
        self.assertIs(bun.get_name(), name)
        self.assertIs(bun.get_price(), price)
