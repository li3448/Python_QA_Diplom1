import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('bun_name, bun_price', [('Флюоресцентная булка', 988), ('Краторная булка', 1255)])
    def test_get_name(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        name = bun.get_name()
        assert bun_name == name

    @pytest.mark.parametrize('bun_name, bun_price',  [('Флюоресцентная булка', 988), ('Краторная булка', 1255)])
    def test_get_price(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        price = bun.get_price()
        assert bun_price == price
