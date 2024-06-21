from unittest.mock import Mock
from praktikum.burger import Burger
from data import BunData, IngredientData, Receipt


class TestBurger:

    def test_set_buns(self):
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_get_price(self):
        mock_bun = Mock()
        burger = Burger()
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 300
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 500

    def test_add_ingredient(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_3 = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_3, mock_ingredient_1]

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = BunData.bun_name
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = IngredientData.ingredient_type
        mock_ingredient.get_name.return_value = IngredientData.ingredient_name
        mock_bun.get_price.return_value = 100
        mock_ingredient.get_price.return_value = 300
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        expected_receipt = Receipt.receipt_body
        assert burger.get_receipt() == expected_receipt

