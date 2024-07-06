from unittest.mock import Mock


class TestBun:
    def test_for_get_name_method(self):
        bun_mock = Mock()
        bun_mock.name = "Краторная булка N-200i"
        bun_mock.price = 1255
        assert bun_mock.name == "Краторная булка N-200i"

    def test_for_get_price_method(self):
        bun_mock = Mock()
        bun_mock.name = "Краторная булка N-200i"
        bun_mock.price = 1255
        assert bun_mock.price == 1255
