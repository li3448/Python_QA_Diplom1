import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import *

class TestBurger:

    def test_get_receipt_successful(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Краторная булка N-200i'
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_1.get_name.return_value = 'Соус фирменный Space Sauce'
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_2.get_name.return_value = 'Говяжий метеорит (отбивная)'
        mock_burger = Mock()
        mock_burger.get_price.return_value = 5590
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.get_price = mock_burger.get_price
        expected_result = '(==== Краторная булка N-200i ====)\n' \
                          '= sauce Соус фирменный Space Sauce =\n' \
                          '= filling Говяжий метеорит (отбивная) =\n' \
                          '(==== Краторная булка N-200i ====)\n' \
                          '\nPrice: 5590'
        assert burger.get_receipt() == expected_result



    @pytest.mark.parametrize(
        "bun_price,ingredient_price",
        [
            [100, 1],
            [0, 10],
            [100, 0]
        ]
    )
    def test_get_price_successful(self, bun_price, ingredient_price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == bun_price * 2 + ingredient_price * 3

    def test_set_buns_successful(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Краторная булка N-200i'
        mock_bun.get_price.return_value = 1255
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_successful(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_1.type = 'SAUCE'
        mock_ingredient_1.name = 'Соус традиционный галактический'
        mock_ingredient_1.price = 15
        mock_ingredient_2 = Mock()
        mock_ingredient_2.type = 'FILLING'
        mock_ingredient_2.name = 'Говяжий метеорит (отбивная)'
        mock_ingredient_2.price = 3000
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient_2]

    def test_remove_ingredient_successful(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.remove_ingredient(0)
        assert mock_ingredient_1 not in burger.ingredients

    def test_move_ingredient_successful(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]
