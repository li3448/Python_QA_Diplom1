import pytest
from unittest.mock import patch, Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from generators import *


@pytest.fixture(scope='function')
def mock_bun():
    with patch('praktikum.burger.Bun') as mock_bun_class:
        mock_bun_instance = mock_bun_class.return_value
        mock_bun_instance.name = bun_name
        mock_bun_instance.price = bun_price
        yield mock_bun_instance


@pytest.fixture(scope='function')
def mock_ingredient():
    with patch('praktikum.burger.Ingredient') as mock_ingredient_class:
        mock_ingredient_instance = mock_ingredient_class.return_value
        mock_ingredient_instance.type = INGREDIENT_TYPE_SAUCE
        mock_ingredient_instance.name = ingredient_name
        mock_ingredient_instance.price = ingredient_price
        yield mock_ingredient_instance


@pytest.fixture(scope='function')
def mock_burger(mock_ingredient):
    with patch.object(Burger, 'add_ingredient') as mock_add_ingredient:
        mock_add_ingredient.return_value = None
        new_burger = Burger()
        new_burger.add_ingredient(mock_ingredient)
        new_burger.add_ingredient(mock_ingredient)
        yield new_burger