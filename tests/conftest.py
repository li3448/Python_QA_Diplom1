import pytest
from unittest.mock import Mock
from praktikum.database import Database
from tests.data import MockBun, MockIngredient, MockIngredient2


@pytest.fixture(scope='function')
def mok_bun():
    bun = Mock()
    bun.get_name.return_value = MockBun.NAME
    bun.get_price.return_value = MockBun.PRICE

    return bun


@pytest.fixture(scope='function')
def mok_ingredient():
    ingredient = Mock()
    ingredient.get_name.return_value = MockIngredient.NAME
    ingredient.get_price.return_value = MockIngredient.PRICE
    ingredient.get_type.return_value = MockIngredient.TYPE
    return ingredient


@pytest.fixture(scope='function')
def mok_ingredient_2():
    ingredient = Mock()
    ingredient.get_name.return_value = MockIngredient2.NAME
    ingredient.get_price.return_value = MockIngredient2.PRICE
    ingredient.get_type.return_value = MockIngredient2.TYPE
    return ingredient


@pytest.fixture(scope='function')
def mock_database_available_buns():
    mock_db = Mock(spec=Database)
    mock_db.available_buns.return_value = [
        Mock(name='Крафтовая булка', price=100),
        Mock(name='Классическая булка', price=50),
        Mock(name='Цельнозерновая булка', price=75),
        Mock(name='Луковая булка', price=90),
        Mock(name='Чесночная булка', price=120),
    ]
    return mock_db

@pytest.fixture(scope='function')
def mock_database_available_ingredients():
    mock_db = Mock(spec=Database)
    mock_db.available_buns.return_value = [
        Mock(name='Крафтовая булка', price=100),
        Mock(name='Классическая булка', price=50),
        Mock(name='Цельнозерновая булка', price=75),
        Mock(name='Луковая булка', price=90),
    ]
    return mock_db


