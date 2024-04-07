from unittest.mock import Mock
from data import Data, ExpectedResult
from praktikum_package.burger import Burger


class TestBurger:

    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = Data.BUN_PRICE

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = Data.INGREDIENT_PRICE

        new_burger = Burger()

        new_burger.set_buns(mock_bun)

        new_burger.add_ingredient(mock_ingredient)

        assert new_burger.get_price() == Data.BUN_PRICE * 2 + Data.INGREDIENT_PRICE

    def test_get_receipt_success(self):

        mock_bun = Mock()
        mock_bun.get_name.return_value = Data.BUN_NAME
        mock_bun.get_price.return_value = Data.BUN_PRICE

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = Data.INGREDIENT_TYPE
        mock_ingredient.get_name.return_value = Data.INGREDIENT_NAME
        mock_ingredient.get_price.return_value = Data.INGREDIENT_PRICE

        new_burger = Burger()
        new_burger.set_buns(mock_bun)
        new_burger.add_ingredient(mock_ingredient)

        assert new_burger.get_receipt() == ExpectedResult.RECEIPT
