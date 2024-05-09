from practicum.burger import Burger
from practicum.bun import Bun
import pytest
import allure
from data import *
from unittest.mock import Mock, patch
from practicum.ingredient import Ingredient


class TestBurger:

    def test_set_buns_name(self):
        mock_bun = Mock()
        mock_bun.configure_mock(name=BurgerData.bun_name, price=BurgerData.bun_price_1)
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == BurgerData.bun_name

    def test_set_buns_price(self):
        mock_bun = Mock()
        mock_bun.configure_mock(name=BurgerData.bun_name, price=BurgerData.bun_price_1)
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.price == BurgerData.bun_price_1
