from praktikum.bun import Bun
from input_data import Data


class TestBun:

    def test_get_name_true_str(self):
        bun = Bun(f'{Data.BUN_NAME}', 23)
        assert isinstance(bun.get_name(), str)
        assert bun.get_name() == Data.BUN_NAME

    def test_get_price_true_float(self):
        bun = Bun(f'{Data.BUN_NAME}', 23.55)
        assert isinstance(bun.get_price(), float)
        assert bun.get_price() == 23.55



