import pytest
from unittest.mock import patch
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from generators_data import generate_random_bun_name, generate_random_bun_price, generate_random_ingredient_name, generate_random_ingredient_price

@pytest.fixture(scope='function')
def bun_name():
    return generate_random_bun_name()

@pytest.fixture(scope='function')
def bun_price():
    return generate_random_bun_price()

@pytest.fixture(scope='function')
def ingredient_name():
    return generate_random_ingredient_name()

@pytest.fixture(scope='function')
def ingredient_price():
    return generate_random_ingredient_price()

@pytest.fixture(scope='function')
def mock_bun(bun_name, bun_price):
    with patch('praktikum.burger.Bun') as MockBun:
        mock_bun_instance = MockBun.return_value
        mock_bun_instance.get_name.return_value = bun_name
        mock_bun_instance.get_price.return_value = bun_price
        yield mock_bun_instance

@pytest.fixture(scope='function')
def mock_ingredient(ingredient_name, ingredient_price):
    with patch('praktikum.burger.Ingredient') as MockIngredient:
        mock_ingredient_instance = MockIngredient.return_value
        mock_ingredient_instance.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_instance.get_name.return_value = ingredient_name
        mock_ingredient_instance.get_price.return_value = ingredient_price
        yield mock_ingredient_instance

@pytest.fixture(scope='function')
def mock_burger(mock_ingredient):
    with patch.object(Burger, 'add_ingredient') as mock_add_ingredient:
        mock_add_ingredient.return_value = None
        new_burger = Burger()
        new_burger.add_ingredient(mock_ingredient)
        new_burger.add_ingredient(mock_ingredient)
        yield new_burger
