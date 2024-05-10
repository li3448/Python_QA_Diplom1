from practicum.bun import Bun
import allure
from data import *


class TestBun:
    @allure.title('Проверка метода присваивания названия для булки')
    def test_get_bun_name(self):
        bun = Bun(BurgerData.bun_name, BurgerData.bun_price_1)
        assert bun.get_name() == BurgerData.bun_name

    @allure.title("Проверка метода присваивания цены для булки")
    def test_get_bun_price(self):
        bun = Bun(BurgerData.bun_name, BurgerData.bun_price_1)
        assert bun.get_price() == BurgerData.bun_price_1
