from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import *


class TestBurger:
    def test_set_buns(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Чиабатта'
        mock_bun.get_price.return_value = 50
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.type = 'FILLING'
        mock_ingredient.name = 'Сыр Чеддер'
        mock_ingredient.price = 10
        mock_ingredient2 = Mock()
        mock_ingredient2.type = 'SAUCE'
        mock_ingredient2.name = 'Барбекю'
        mock_ingredient2.price = 15
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient2)
        assert burger.ingredients == [mock_ingredient, mock_ingredient2]

    def test_remove_ingredient_successful(self):
        mock_ingredient = Mock()
        mock_ingredient2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient, mock_ingredient2]
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient_successful(self):
        mock_ingredient = Mock()
        mock_ingredient2 = Mock()
        burger = Burger()
        burger.ingredients = [mock_ingredient, mock_ingredient2]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient]
