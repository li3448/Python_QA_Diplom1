import pytest
from unittest.mock import Mock
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.burger import Burger

@pytest.fixture
def test_bun():
    return Bun(name="Kratorskaya", price=1255)


@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_price.return_value = 2
    mock.get_name.return_value = "Test Bun"
    return mock

def create_mock_ingredient(name, price, type):
    mock = Mock(spec=Ingredient)
    mock.get_price.return_value = price
    mock.get_name.return_value = name
    mock.get_type.return_value = type
    return mock

@pytest.fixture
def mock_ingredient():
    return create_mock_ingredient("Test Ingredient", 1, "Filling")

@pytest.fixture
def burger(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger

@pytest.fixture
def burger_with_ingredients(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(create_mock_ingredient("Ingredient 1", 1, "Filling"))
    burger.add_ingredient(create_mock_ingredient("Ingredient 2", 1, "Filling"))
    burger.add_ingredient(create_mock_ingredient("Ingredient 3", 1, "Filling"))
    return burger

