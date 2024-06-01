from praktikum.bun import Bun
from data import Data


class TestBun:
    def test_get_name_bun_return_name_bun(self, bun_instance, mock_bun):
        assert bun_instance.get_name() == Data.BUN_NAME

    def test_get_price_bun_return_price_bun(self, bun_instance, mock_bun):
        assert bun_instance.get_price() == Data.BUN_PRICE
