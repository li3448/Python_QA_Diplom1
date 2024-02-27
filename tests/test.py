from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun


class Test:

    def test_get_price(self):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 200.00
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 300.00
        burger = Burger()

        assert burger.get_price() == 700.00

