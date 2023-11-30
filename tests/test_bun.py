from praktikum.bun import Bun


class TestBun:

    def test_get_name_correct_name_shown(self):

        bun = Bun("White bun", 40.5)

        assert bun.get_name() == "White bun"

    def test_get_price_correct_price_shown(self):

        bun = Bun("White bun", 40.5)

        assert bun.get_price() == 40.5