from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestBurger:
    def test_set_buns_true(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_added(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient_true(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_true(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == second_ingredient

    def test_get_price_true(self, burger, ingredient, bun):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 2553

    def test_get_receipt_true(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        second_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        burger.add_ingredient(second_ingredient)

        for ingredient in burger.ingredients:
            receipt_text_list = [burger.get_price(), bun.get_name(),
                                 ingredient.get_name(), ingredient.get_type().lower()]
            for receipt_text in receipt_text_list:
                assert str(receipt_text) in burger.get_receipt()
