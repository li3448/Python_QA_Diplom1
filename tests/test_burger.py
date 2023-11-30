import pytest
from data import filling, sauce
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns_successful_set(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "White bun"
        mock_bun.get_price.return_value = 40.5
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    @pytest.mark.parametrize("ingredient", [
        [filling],
        [sauce],
        [filling, sauce]
    ])
    def test_add_ingredient_successful_adding(self, ingredient):
        burger = Burger()

        burger.add_ingredient(ingredient)

        assert burger.ingredients.count(ingredient) == 1
        assert ingredient in burger.ingredients

    def test_remove_ingredient_successful_remove(self):
        burger = Burger()

        burger.ingredients = [filling, sauce]
        burger.remove_ingredient(0)

        assert filling not in burger.ingredients

    def test_move_ingredient_successful_move(self):
        burger = Burger()

        burger.ingredients = [filling, sauce]
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [sauce, filling]

    def test_get_price_correct_price_calculated(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 40.5
        mock_filling = Mock()
        mock_filling.get_price.return_value = 200
        mock_sauce = Mock()
        mock_sauce.get_price.return_value = 30.4

        burger.bun = mock_bun
        burger.ingredients = [mock_filling, mock_sauce]

        assert burger.get_price() == 311.4

    def test_get_receipt_correct_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "White bun"
        mock_filling = Mock()
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "Cutlet"
        mock_sauce = Mock()
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "Hot sauce"
        mock_burger = Mock()
        mock_burger.get_price.return_value = 311.4

        burger.bun = mock_bun
        burger.ingredients = [mock_filling, mock_sauce]
        burger.get_price = mock_burger.get_price

        expected_receipt = f'(==== White bun ====)\n' \
                           f'= filling Cutlet =\n' \
                           f'= sauce Hot sauce =\n' \
                           f'(==== White bun ====)\n' \
                           f'\nPrice: 311.4'

        assert burger.get_receipt() == expected_receipt