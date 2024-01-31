from unittest.mock import Mock

from Diplom_1.praktikum.burger import Burger
from Diplom_1.praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 1

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 100 * 2 + 1 * 3

    def test_remove_ingredient(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 2

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 3

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(1)

        assert burger.get_price() == 100 * 2 + 2

    def test_move_ingredient(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 2

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 3

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        burger.remove_ingredient(1)

        assert burger.get_price() == 100 * 2 + 3

    def test_get_receipt_contains_bun_name(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Unique-Bun-Name"
        mock_bun.get_price.return_value = 0

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "Unique-Ingredient-Name"
        mock_ingredient.get_price.return_value = 0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert "Unique-Bun-Name" in burger.get_receipt()

    def test_get_receipt_contains_ingredient_name(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Unique-Bun-Name"
        mock_bun.get_price.return_value = 0

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "Unique-Ingredient-Name"
        mock_ingredient.get_price.return_value = 0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert "Unique-Ingredient-Name" in burger.get_receipt()

