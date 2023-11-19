import pytest
import ingredient_types
from burger import Burger
from bun import Bun
from ingredient import Ingredient


class TestBurger:
    def test_set_buns_bun_added_successfully(self):
        bun = Bun("булочка с кунжутом", 100)
        burger = Burger()
        burger.set_buns(bun)
        expected_result = burger.bun.get_name()
        assert expected_result == "булочка с кунжутом"

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'garlic', 8.5],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'bacon', 25]
    ])
    def test_add_ingredient_ingredient_added_successfully(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'cheese', 6.5],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'pickles', 12.5]
    ])
    def test_remove_ingredient_ingredient_removed_successfully(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_ingredient_move_successfully(self):
        burger = Burger()
        ingredient_1 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'pickles', 12.5)
        burger.add_ingredient(ingredient_1)
        ingredient_2 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'bacon', 25)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients.index(ingredient_2) == 0
