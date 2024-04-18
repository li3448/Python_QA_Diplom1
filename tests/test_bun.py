import pytest
from praktikum.bun import Bun
from data import Values


class TestBun:

    def test_get_name(self):
        bun = Bun(Values.BUN_NAME, Values.BUN_PRICE)
        assert bun.get_name() == Values.BUN_NAME

    @pytest.mark.parametrize('bun_prices', [Values.BUN_PRICES[0],
                                           Values.BUN_PRICES[1],
                                           Values.BUN_PRICES[2],
                                           Values.BUN_PRICES[3]])
    def test_get_price(self, bun_prices):
        bun = Bun(Values.BUN_NAME, bun_prices)
        assert bun.get_price() == bun_prices
