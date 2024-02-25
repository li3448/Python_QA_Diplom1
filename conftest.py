import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from data import buns, ingreds


@pytest.fixture
def bun():
    return Bun("black bun", 100)


@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)


@pytest.fixture
def burger():

    mock_bun = Mock()
    mock_bun.get_price.return_value = buns[0]['price']
    mock_bun.get_name.return_value = buns[0]['name']

    mock_ingred0 = Mock()
    mock_ingred0.get_type.return_value = ingreds[0]['type']
    mock_ingred0.get_name.return_value = ingreds[0]['name']
    mock_ingred0.get_price.return_value = ingreds[0]['price']

    mock_ingred1 = Mock()
    mock_ingred1.get_type.return_value = ingreds[1]['type']
    mock_ingred1.get_name.return_value = ingreds[1]['name']
    mock_ingred1.get_price.return_value = ingreds[1]['price']

    burger = Burger()
    burger.bun = mock_bun
    burger.ingredients = [mock_ingred0, mock_ingred1]

    return burger
