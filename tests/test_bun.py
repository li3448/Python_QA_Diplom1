from bun import Bun
from data.data import TestData


class TestBun:

    def test_default_bun_name_true(self):
        bun = Bun(
            *TestData.BUNS_LIST[0]
        )
        assert bun.name == 'bun name 1'

    # тест конструктора
    def test_default_bun_price_true(self):
        bun = Bun(
            *TestData.BUNS_LIST[0]
        )
        assert bun.price == 1

    def test_get_name(self):
        bun = Bun(
            *TestData.BUNS_LIST[0]
        )
        assert bun.get_name() == 'bun name 1'

    def test_get_price(self):
        bun = Bun(
            *TestData.BUNS_LIST[0]
        )
        assert bun.get_price() == 1