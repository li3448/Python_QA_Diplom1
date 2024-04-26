from bun import Bun


class TestBun:

    # тест конструктора
    test_bun = (
        'bun name',
        1
    )

    def test_default_bun_name_true(self):
        bun = Bun(*self.test_bun)
        assert bun.name == 'name'

    # тест конструктора
    def test_default_bun_price_true(self):
        bun = Bun(*self.test_bun)
        assert bun.price == 1

    def test_get_name(self):
        bun = Bun(*self.test_bun)
        assert bun.get_name() == 'name'

    def test_get_price(self):
        bun = Bun(*self.test_bun)
        assert bun.get_price() == 1