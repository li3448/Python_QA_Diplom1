from conftest import bun
class Test_Bun:

    def test_bun_get_name_positive(self, bun):
        assert bun.get_name() == bun.name

    def test_bun_get_price_positive(self, bun):
        assert bun.get_price() ==  bun.price