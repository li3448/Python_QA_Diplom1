import pytest
from praktikum.praktikum import Bun
from praktikum.burger import Burger


@pytest.fixture(params=[
    ('Baguette 123', 100.99),
    ('Бриошь', 150)
])
def bun(request):
    name, price = request.param
    return Bun(name, price)


@pytest.fixture
def test_burger():
    return Burger()
