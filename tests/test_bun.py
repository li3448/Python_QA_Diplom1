from utils import generate_random_string, generate_random_float
from praktikum import Bun


class TestBun:
    def test_bun_name_price(self):
        name = generate_random_string(10)
        price = generate_random_float()
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
