import pytest
from Diplom_1.bun import Bun


class TestBun:

    def test_get_name_get_name_of_bun(self):
        bun = Bun(name = 'Сливочный', price = 2.3)
        assert bun.get_name() == 'Сливочный'

    def test_get_price_get_name_of_bun(self):
        bun = Bun(name='Сливочный', price=2.3)
        assert bun.get_price() == 2.3
