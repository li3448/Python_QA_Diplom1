from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from data import Data

import pytest


@pytest.fixture(scope='function')
def mock_bun_get_price():
    mock_bun = Mock()
    mock_bun.get_price.return_value = Data.BUN_PRICE

    return mock_bun


@pytest.fixture(scope='function')
def mock_bun_get_name(mock_bun_get_price):
    mock_bun_get_price.get_name.return_value = Data.BUN_NAME


@pytest.fixture(scope='function')
def mock_ingredient_get_price():
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = Data.INGREDIENT_PRICE

    return mock_ingredient


@pytest.fixture(scope='function')
def mock_ingredient_get_name_and_get_type(mock_ingredient_get_price):
    mock_ingredient_get_price.get_name.return_value = Data.INGREDIENT_NAME
    mock_ingredient_get_price.get_type.return_value = Data.INGREDIENTS_TYPE


@pytest.fixture(scope='function')
def bun_instance():
    bun = Bun(name=Data.BUN_NAME, price=Data.BUN_PRICE)

    return bun


@pytest.fixture(scope='function')
def ingredient_instance():
    ingredient = Ingredient(name=Data.BUN_NAME, price=Data.BUN_PRICE, ingredient_type=Data.INGREDIENTS_TYPE)

    return ingredient


@pytest.fixture(scope='function')
def burger_instance():
    burger = Burger()

    return burger


@pytest.fixture(scope='function')
def database_instance():
    database = Database()

    return database
