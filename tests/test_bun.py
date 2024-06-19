from bun import Bun
from helpers.generate import generate_name, generate_price


class TestBun:
    def test_bun_get_name(self):
        name = generate_name()
        price = generate_price()

        bun = Bun(name=name, price=price)

        assert bun.get_name() == name

    def test_bun_get_price(self):
        name = generate_name()
        price = generate_price()

        bun = Bun(name=name, price=price)

        assert bun.get_price() == price
