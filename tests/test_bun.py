
class TestBun:
    def test_bun_returns_correct_name(self, bun, bun_name):
        assert bun.get_name() == bun_name

    def test_bun_returns_correct_price(self, bun, bun_price):
        assert bun.get_price() == bun_price
