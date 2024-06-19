from bun import Bun
# import pytest


class TestBun:
    def test_get_name(self):
        bun = Bun('HAMBERGER', 100.50)
        assert bun.get_name() == 'HAMBERGER'

    def test_get_price(self):
        bun = Bun('HAMBERGER', 100.50)
        assert bun.get_price() == 100.50
