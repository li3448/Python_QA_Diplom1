from data import Data


class TestBun:
    def test_name_of_bun_true(self, bun):
        assert bun.name == Data.bun_name, 'Имя булки при создании записывается неверно'

    def test_price_of_bun_true(self, bun):
        assert bun.price == Data.bun_price, 'Цена булки при создании записывается неверно'

    def test_get_name_return_correct_name(self, bun):
        result = bun.get_name()
        assert result == Data.bun_name

    def test_get_price_return_correct_price(self, bun):
        result = bun.get_price()
        assert result == Data.bun_price
