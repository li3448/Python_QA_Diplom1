class TestBun:
    def test_name_matches_expected(self, test_bun):
        assert test_bun.get_name() == "Kratorskaya", "Название булочки должно совпадать с переданным значением"

    def test_name_is_string(self, test_bun):
        assert isinstance(test_bun.get_name(), str), "Название булочки должно быть строкой"

    def test_price_matches_expected(self, test_bun):
        assert test_bun.get_price() == 1255, "Цена булочки должна совпадать с переданным значением"

    def test_price_is_int(self, test_bun):
        assert isinstance(test_bun.get_price(), int), "Цена булочки должна быть целым числом"
