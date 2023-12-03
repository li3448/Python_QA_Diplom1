from unittest.mock import Mock

import pytest

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import *


class TestBurger:

    @pytest.mark.parametrize('name, price', [
        ["black bun", 100],
        ["white bun", 200],
        ["red bun", 300]
                             ])
    def test_set_buns(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)

        assert burger.bun == bun

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [INGREDIENT_TYPE_SAUCE, "hot sauce", 88.25],
        [INGREDIENT_TYPE_FILLING, "dinosaur", -100.78]
    ])
    def test_add_ingredient(self, ingredient_type, name, price):
        burger = Burger()
        ingredient = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 88.25)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient('mayonnaise', INGREDIENT_TYPE_SAUCE, 0.5)
        ingredient2 = Ingredient('tomato', INGREDIENT_TYPE_FILLING, 0.7)
        ingredient3 = Ingredient('lettuce', INGREDIENT_TYPE_FILLING, 0.3)
        burger.ingredients = [ingredient1, ingredient2, ingredient3]
        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    def test_get_price(self):
        burger = Burger()
        bun = Bun('sesame', 2.0)
        ingredient1 = Ingredient('mayonnaise', INGREDIENT_TYPE_SAUCE, 0.5)
        ingredient2 = Ingredient('tomato', INGREDIENT_TYPE_FILLING, 0.7)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        assert burger.get_price() == 5.2

    def test_get_receipt(self):
        burger = Burger()
        burger.bun = Mock(get_name=Mock(return_value='Bun'), get_price=Mock(return_value=2.1))
        ingredient1 = Mock(get_type=Mock(return_value='Ingredient'), get_name=Mock(return_value='Ingredient 1'),
                           get_price=Mock(return_value=1.8))
        ingredient2 = Mock(get_type=Mock(return_value='Ingredient'), get_name=Mock(return_value='Ingredient 2'),
                           get_price=Mock(return_value=2.0))
        burger.ingredients = [ingredient1, ingredient2]

        receipt = burger.get_receipt()

        expected_receipt = "(==== Bun ====)\n" \
                           "= ingredient Ingredient 1 =\n" \
                           "= ingredient Ingredient 2 =\n" \
                           "(==== Bun ====)\n"\
                           '\n'\
                           "Price: 8.0"
        assert receipt == expected_receipt

