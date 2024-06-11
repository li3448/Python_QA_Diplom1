import pytest
from praktikum.bun import Bun


#  tests bun.py methods
class TestBun:

    # test get_name() for a bun
    @pytest.mark.parametrize('name',
                             [
                                 "My sweet bun",
                                 "Ля-ля-тополя",
                                 "r54e Cosmic",
                                 "ф"
                             ])
    def test_get_name_returns_bun_name(self, name):
        bun = Bun(name, 555)

        assert bun.get_name() == name

    # test get_price() for a bun
    @pytest.mark.parametrize('price',
                             [
                                 555,
                                 444.55,
                                 123 + 456,
                                 17 - 99,
                                 0
                             ])
    def test_get_price_returns_bun_price(self, price):
        bun = Bun('Летающая кислотная булка', price)

        assert bun.get_price() == price
