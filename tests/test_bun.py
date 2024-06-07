import pytest
from generators_data import generate_random_bun_name, generate_random_bun_price
from praktikum.bun import Bun

@pytest.fixture(scope='function')
def bun_name():
    return generate_random_bun_name()

@pytest.fixture(scope='function')
def bun_price():
    return generate_random_bun_price()

@pytest.fixture(scope='function')
def bun(bun_name, bun_price):
    return Bun(bun_name, bun_price)

class TestBun:
    def test_bun_returns_correct_name(self, bun, bun_name):
        assert bun.get_name() == bun_name

    def test_bun_returns_correct_price(self, bun, bun_price):
        assert bun.get_price() == bun_price
