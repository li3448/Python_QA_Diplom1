import pytest
from praktikum.bun import Bun
from data import Data


class TestBun:

    def test_get_name_result(self):
        bun = Bun(Data.BUN_NAME[0], Data.BUN_PRICE[0])
        assert bun.get_name() == Data.BUN_NAME[0]

    @pytest.mark.parametrize('name, price',
                             [(Data.BUN_NAME[0], Data.BUN_PRICE[0]),
                              (Data.BUN_NAME[1], Data.BUN_PRICE[1])])
    def test_get_price_result(self, name, price):
        bun = Bun(name, price)
        result = [bun.get_name(), bun.get_price()]
        assert result == [name, price],  'Ответ не соответствует ожидаемому'

