class TestBun:

    def test_get_name(self, bun):
        assert bun.get_name() == bun.name

    def test_get_price(self, bun):
        assert bun.get_price() == bun.price
