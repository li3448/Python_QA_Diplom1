from practicum.bun import Bun
import pytest
import allure
from data import *


class TestBun:
    @allure.title('Проверка метода присваивания названия для булки')
    def test_get_bun_name(self):
        bun = Bun(Burger.bun_name, Burger.bun_price_1)
        assert bun.get_name() == Burger.bun_name

    @allure.title("Проверка метода присваивания цены для булки")
    def test_get_bun_price(self):
        bun = Bun(Burger.bun_name, Burger.bun_price_1)
        assert bun.get_price() == Burger.bun_price_1
