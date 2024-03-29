class TestBun:
    def test_get_name_true(self, bun):
        assert bun.get_name() == 'Крейзи_Булка'

    def test_get_price_true(self, bun):
        assert bun.get_price() == 999
