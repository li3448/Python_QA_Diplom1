from praktikum.bun import Bun


class TestBun:

    def test_name_price_true(self):
        bun = Bun('Булка Ньютона', 2.5)

        assert bun.name == 'Булка Ньютона' and bun.price == 2.5

    def test_get_name_bun_true(self):
        bun = Bun('Булка Ньютона', 2.5)

        assert bun.get_name() == 'Булка Ньютона'

    def test_get_price_bun_true(self):
        bun = Bun('Булка Ньютона', 2.5)

        assert bun.get_price() == 2.5
