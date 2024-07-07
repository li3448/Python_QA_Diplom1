import pytest
from bun import Bun


@pytest.mark.parametrize("name, price", [
    ('Sesame', 1.0),
    ('Whole Wheat', 1.2),
    ('Gluten-Free', 1.3),
])
def test_bun_initialization(name, price):
    bun = Bun(name, price)
    assert bun.name == name
    assert bun.price == price


@pytest.mark.parametrize("initial_price, new_price", [
    (1.0, 1.5),
    (1.2, 1.3),
    (1.3, 1.0),
])
def test_bun_price_update(initial_price, new_price):
    bun = Bun('Sesame', initial_price)
    bun.price = new_price
    assert bun.price == new_price
