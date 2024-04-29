import pytest

from data import Data
from praktikum.burger import Burger


class TestBurger:

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0, 'Ответ не соответствует ожидаемому'

    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        [burger.add_ingredient(mock_ingredient) for _ in range(2)]
        before_move_ingredient = burger.ingredients[0]
        burger.move_ingredient(0, 1)
        after_move_ingredient = burger.ingredients[1]
        assert before_move_ingredient == after_move_ingredient, 'Ответ не соответствует ожидаемому'

    def test_get_price(self, mock_ingredient, mock_bun):
        burger = Burger()
        mock_bun.get_price.return_value = Data.BUN_PRICE[0]
        mock_ingredient.get_price.return_value = Data.ING_PRICE
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        result_price = Data.BUN_PRICE[0] * 2 + Data.ING_PRICE
        assert burger.get_price() == result_price, 'Ответ не соответствует ожидаемому'

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        mock_bun.get_price.return_value = Data.BUN_PRICE[0]
        mock_ingredient.get_price.return_value = Data.ING_PRICE
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        assert burger.get_receipt() == Data.EXPECTED_RESULT, 'Ответ не соответствует ожидаемому'
