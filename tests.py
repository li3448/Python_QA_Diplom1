
class TestBun:

    def test_get_name_get_name_of_bun(self, bun_create):
        assert bun_create.get_name() == 'Сливочный'

    def test_get_price_get_name_of_bun(self, bun_create):
        assert bun_create.get_price() == 2.5 and type(bun_create.get_price()) == float

