import pytest
from unittest.mock import Mock
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.burger import Burger
from Diplom_1.praktikum.database import Database
from Diplom_1.praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def test_bun():
    return Bun(name="Kratorskaya", price=1255)


@pytest.fixture
def database():
    return Database()

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 2
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Test Ingredient"
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_price.return_value = 1
    return ingredient

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
    ingredients = [Mock(spec=Ingredient) for _ in range(3)]
    for i, ingredient in enumerate(ingredients):
        ingredient.get_name.return_value = f"Ingredient {i}"
        ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient.get_price.return_value = 1
        burger.add_ingredient(ingredient)
    return burger


@pytest.fixture
def database():
    return Database()

@pytest.fixture
def mock_bun():
    return Bun("test bun", 100)

@pytest.fixture
def mock_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 100)

@pytest.fixture
def mock_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "test filling", 200)

