from unittest.mock import patch, Mock

import pytest
from bun import Bun
from burger import Burger
from database import Database

class TestBun:
    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_get_name(self, index):
        database = Database()
        bun_name = database.buns[index].get_name()
        bun_price = database.buns[index].get_price()

        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_get_price(self, index):
        database = Database()
        bun_name = database.buns[index].get_name()
        bun_price = database.buns[index].get_price()

        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price

class TestBurger:
    @patch('Diplom_1.bun.Bun')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        mock_bun = mock_bun.return_value
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 50

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    @patch('Diplom_1.ingredient.Ingredient')
    @pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5])
    def test_add_ingredient(self, mock_ingredient, index):
        burger = Burger()
        database = Database()

        database_ingredient = database.ingredients

        mock_ingredient = mock_ingredient.return_value
        mock_ingredient.get_type.return_value = database_ingredient[index].get_type()
        mock_ingredient.get_name.return_value = database_ingredient[index].get_name()
        mock_ingredient.get_price.return_value = database_ingredient[index].get_price()

        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0].get_type() == database_ingredient[index].get_type()
        assert burger.ingredients[0].get_name() == database_ingredient[index].get_name()
        assert burger.ingredients[0].get_price() == database_ingredient[index].get_price()



