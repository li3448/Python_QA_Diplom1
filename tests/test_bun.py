import allure
import pytest
from bun import Bun
from data import BurgerConsist as bc


class TestBun:
    @allure.title('проверка получения названия булки - метод get_name')
    def test_get_name(self):
        bun = Bun(bc.SECOND_BUN_NAME, bc.SECOND_BUN_PRICE)
        assert bun.get_name() == bc.SECOND_BUN_NAME


    @allure.title('проверка получения стоимости булки - метод get_price')
    def test_get_price(self):
        bun = Bun(bc.SECOND_BUN_NAME, bc.SECOND_BUN_PRICE)
        assert bun.get_price() == bc.SECOND_BUN_PRICE


    @allure.title('проверка сборки бургера с пустым и незаданным (None) названием булки')
    @pytest.mark.parametrize('name', ['', None])
    def test_without_bun_name(self, name):
        bun = Bun(name, bc.SECOND_BUN_PRICE)
        assert bun.name == name


    @allure.title('проверка сброки бургера с нулевой, пустой и незаданной (None) стоимостью булки')
    @pytest.mark.parametrize('price', [0.0, '', None])
    def test_without_bun_price(self, price):
        bun = Bun(bc.SECOND_BUN_PRICE, price)
        assert bun.price == price

