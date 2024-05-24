import pytest
from bun import Bun
from burger import Burger
from ingredient import Ingredient


class TestBurgerFunction:
    def test_burger_set_buns(self):
        burger = Burger()
        bun = Bun('Лунная булка KJ-400', 1100)
        burger.set_buns(bun)
        assert burger.bun.get_name() == 'Лунная булка KJ-400'

    def test_burger_add_ingredient(self):
        burger = Burger()
        fill = Ingredient('Соус', 'Соус фирменный Space Sauce', 80)
        assert burger.add_ingredient(fill) == 1
        