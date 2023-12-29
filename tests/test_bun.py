from praktikum.bun import Bun


class TestBun:
    def test_get_name_create_new_bun_check_name(self):
        new_bun = Bun('Булочка', 10.5)
        assert new_bun.get_name() == 'Булочка'

    def test_get_name_create_new_bun_check_price(self):
        new_bun = Bun('Булочка', 10.5)
        assert new_bun.get_price() == 10.5
