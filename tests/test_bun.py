from data import TestData


class TestBun:
    def test_bun_get_name(self):
        assert TestData.bun.get_name() == 'Сэндвич с вогонской плесенью', 'Unable to get bun name'

    def test_bun_get_price(self):
        assert TestData.bun.get_price() == 1500, 'Unable to get bun price'
