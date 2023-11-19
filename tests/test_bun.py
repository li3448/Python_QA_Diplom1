from bun import Bun


class TestBun:
    def test_get_name_valid_name_returned_correct_name_bun(self):
        my_bun = Bun("булочка с кунжутом", 100)
        expected_result = my_bun.get_name()
        assert expected_result == "булочка с кунжутом"

    def test_get_price_valid_price_returned_correct_price_bun(self):
        my_bun = Bun("булочка с кунжутом", 100)
        expected_result = my_bun.get_price()
        assert expected_result == 100



