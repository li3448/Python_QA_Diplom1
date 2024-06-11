from praktikum.burger import Burger
from conftest import *


# tests burger.py methods
class TestBurger:
    # tests set_buns()
    def test_set_buns_successful(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # tests add_ingredients()
    def test_add_ingredients_add_two_successful(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert len(burger.ingredients) == 2

    # tests remove_ingredients()
    def test_remove_ingredients_successful(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    # tests move_ingredients()
    def test_move_ingredients_successful(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger_sauce = burger.add_ingredient(mock_sauce)
        burger_filling = burger.add_ingredient(mock_filling)
        burger.ingredients = [burger_sauce, burger_filling]
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == burger_filling

    # tests get_price()
    def test_get_price(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_price = MockSamples.mock_bun_price * 2 + MockSamples.mock_filling_price + MockSamples.mock_sauce_price
        assert burger.get_price() == expected_price

    # tests get_receipt ()
    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_receipt() == MockSamples.mock_receipt
