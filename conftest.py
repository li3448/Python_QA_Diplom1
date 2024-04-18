import pytest
from unittest.mock import Mock
from data import Values

@pytest.fixture(scope='function')
def mocked_bun():
    mocked_bun = Mock()
    mocked_bun.get_price.return_value = Values.BUN_PRICE
    mocked_bun.get_name.return_value = Values.BUN_NAME
    return mocked_bun

@pytest.fixture(scope='function')
def mocked_ingredient():
    mocked_ingredient = Mock()
    mocked_ingredient.get_price.return_value = Values.INGREDIENT_PRICE
    mocked_ingredient.get_name.return_value = Values.INGREDIENT_NAME
    mocked_ingredient.get_type.return_value = Values.INGREDIENT_TYPE
    return mocked_ingredient
