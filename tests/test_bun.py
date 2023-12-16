from bun import Bun


class TestBun:
    def test_bun_constructor_name(self):
        my_bun = Bun('bulka', 200)
        assert my_bun.name == 'bulka'

    def test_bun_constructor_price(self):
        my_bun = Bun('bulka', 200)
        assert my_bun.price == 200

    def test_get_bun_name(self):
        my_bun = Bun('bulka', 200)
        assert my_bun.get_name() == 'bulka'

    def test_get_bun_price(self):
        my_bun = Bun('bulka2', 600)
        assert my_bun.get_price() == 600
