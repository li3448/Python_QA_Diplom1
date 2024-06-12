import pytest
from unittest.mock import patch
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from generators_data import generate_random_bun_name, generate_random_bun_price
from praktikum.bun import Bun

@pytest.fixture
def mock_add_ingredients():
    class MockAddIngredients:
        def __init__(self):
            self.ingredients = ['meat', 'bun', 'sauce']
        
        def move_ingredient(self, old_index, new_index):
            ingredient = self.ingredients.pop(old_index)
            self.ingredients.insert(new_index, ingredient)
    
    return MockAddIngredients()

@pytest.fixture(scope='function')
def mock_bun():
    with patch('praktikum.burger.Bun') as MockBun:
        mock_bun_instance = MockBun.return_value
        yield mock_bun_instance

@pytest.fixture(scope='function')
def mock_ingredient():
    with patch('praktikum.burger.Ingredient') as MockIngredient:
        mock_ingredient_instance = MockIngredient.return_value
        mock_ingredient_instance.get_type.return_value = INGREDIENT_TYPE_SAUCE
        yield mock_ingredient_instance

@pytest.fixture(scope='function')
def mock_burger(mock_ingredient):
    with patch.object(Burger, 'add_ingredient') as mock_add_ingredient:
        mock_add_ingredient.return_value = None
        new_burger = Burger()
        new_burger.add_ingredient(mock_ingredient)
        new_burger.add_ingredient(mock_ingredient)
        yield new_burger

@pytest.fixture(scope='function')
def bun():
    name = generate_random_bun_name()
    price = generate_random_bun_price()
    return Bun(name, price)
