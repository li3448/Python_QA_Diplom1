from unittest.mock import Mock, patch
from praktikum.ingredient_types import *
import praktikum.ingredient_types
from praktikum.burger import Burger
from conftest import mock_bun, mock_ingredient

class TestBurger:
    def test_set_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        mock_ingredient2 = Mock()
        mock_ingredient2.type = INGREDIENT_TYPE_FILLING
        mock_ingredient2.name = 'dinosaur'
        mock_ingredient2.price = 200
        burger.ingredients = [mock_ingredient, mock_ingredient2]
        burger.remove_ingredient(1)
        assert burger.ingredients == [mock_ingredient]

    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        mock_ingredient2 = Mock()
        mock_ingredient2.type = INGREDIENT_TYPE_FILLING
        mock_ingredient2.name = 'dinosaur'
        mock_ingredient2.price = 200
        burger.ingredients = [mock_ingredient, mock_ingredient2]
        burger.move_ingredient(0,1)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient]

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        mock_bun.get_price.return_value = 100
        mock_ingredient.get_price.return_value = 100
        mock_ingredient2 = Mock()
        mock_ingredient2.type = INGREDIENT_TYPE_FILLING
        mock_ingredient2.name = 'dinosaur'
        mock_ingredient2.price = 200
        mock_ingredient2.get_price.return_value = 200
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient, mock_ingredient2]
        expectation = 2 * mock_bun.price + mock_ingredient2.price + mock_ingredient.price
        assert burger.get_price() == expectation

