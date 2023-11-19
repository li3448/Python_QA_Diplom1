import pytest

import ingredient_types
from burger import Burger
from bun import Bun
from ingredient import Ingredient


class TestBurger:
    def test_set_buns_bun_added_successfully(self):
        my_bun = Bun("булочка с кунжутом", 100)
        my_burger = Burger()
        my_burger.set_buns(my_bun)
        expected_result = my_burger.bun.get_name()
        assert expected_result == "булочка с кунжутом"

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'garlic', 8.5],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'bacon', 25]
    ])
    def test_add_ingredient_ingredient_added_successfully(self, ingredient_type, name, price):
        my_ingredient = Ingredient(ingredient_type, name, price)
        my_burger = Burger()
        my_burger.add_ingredient(my_ingredient)
        assert len(my_burger.ingredients) == 1

    def test_remove_ingredient_ingredient_removed_successfully(self, ingredient_type, name, price):
        my_ingredient = Ingredient(ingredient_type, name, price)
        my_burger = Burger()
        my_burger.add_ingredient(my_ingredient)
        assert len(my_burger.ingredients) == 1