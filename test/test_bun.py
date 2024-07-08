class TestBun:

    def test_bun_get_name_positive(self, bun):
        assert bun.get_name() == "black bun"

    def test_bun_get_price_positive(self, bun):
        assert bun.get_price() == 100