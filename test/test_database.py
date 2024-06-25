from praktikum.burger import Burger
from input_data import Data
from unittest.mock import Mock


class TestBurger:

    def test_set_buns_bon_name_true(self):
        burger = Burger()
        burger.set_buns(Data.BUN_NAME)
        assert burger.bun == Data.BUN_NAME

    def test_add_ingredient_list_with_ingredient_true(self):
        burger = Burger()
        burger.add_ingredient(Data.BURGER_INGREDIENT_CHEESE)
        assert burger.ingredients == [Data.BURGER_INGREDIENT_CHEESE]

    def test_remove_ingredient_from_list_success(self):
        burger = Burger()
        burger.add_ingredient(Data.BURGER_INGREDIENT_CHEESE)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_remove_ingredient_true(self):
        burger = Burger()
        burger.add_ingredient(Data.BURGER_INGREDIENT_CHEESE)
        burger.remove_ingredient(0)
        assert Data.BURGER_INGREDIENT_CHEESE not in burger.ingredients

    def test_move_ingredient_true(self):
        burger = Burger()
        burger.add_ingredient(Data.BURGER_INGREDIENT_CHEESE)
        burger.add_ingredient(Data.BURGER_INGREDIENT_BEACON)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == Data.BURGER_INGREDIENT_BEACON
        assert burger.ingredients[1] == Data.BURGER_INGREDIENT_CHEESE




