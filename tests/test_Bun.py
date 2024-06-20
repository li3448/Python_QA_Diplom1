import allure
import pytest
from bun import Bun


class TestBun:
    @allure.description('Имя булки')
    @pytest.mark.parametrize('name_bun', ['abcde', '1abcd', '123$#', '     ', '123 4'])
    def test_get_name(self, name_bun):
        bun = Bun(name_bun, 100.50)
        assert bun.get_name() == name_bun

    @allure.description('Цена булки')
    @pytest.mark.parametrize('price', ['abcde', '1abcd', '123$#', '     ', '1234'])
    def test_get_price(self, price):
        bun = Bun('HAMBERGER', price)
        assert bun.get_price() == price
