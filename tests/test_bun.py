from bun import Bun
from helpers.generate import generate_name, generate_price


def test_bun_get_name_price():
    name = generate_name()
    price = generate_price()

    bun = Bun(name=name, price=price)

    assert bun.get_name() == name and bun.get_price() == price
