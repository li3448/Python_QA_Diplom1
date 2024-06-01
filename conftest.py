from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import Data

import pytest


@pytest.fixture(scope='function')
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = Data.BUN_NAME
    bun.get_price.return_value = Data.BUN_PRICE

    return bun


@pytest.fixture(scope='function')
def bun_instance():
    bun = Bun(name=Data.BUN_NAME, price=Data.BUN_PRICE)

    return bun


@pytest.fixture(scope='function')
def ingredient_instance():
    ingredient = Ingredient(name=Data.BUN_NAME, price=Data.BUN_PRICE, ingredient_type=Data.INGREDIENTS_TYPE)

    return ingredient
