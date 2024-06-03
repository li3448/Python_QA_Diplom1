import pytest
from unittest.mock import Mock
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.burger import Burger
from Diplom_1.praktikum.database import Database



@pytest.fixture
def test_bun():
    return Bun(name="Kratorskaya", price=1255)

@pytest.fixture
def mock_bun():
    return Mock()

@pytest.fixture
def mock_ingredient():
    return Mock()
@pytest.fixture
def mock_bun():
    class MockBun(Bun):
        def __init__(self):
            self.name = "Sesame Bun"
            self.price = 1.5

        def get_name(self):
            return self.name

        def get_price(self):
            return self.price

    return MockBun()

@pytest.fixture
def mock_ingredient():
    class MockIngredient(Ingredient):
        def __init__(self, name="Lettuce", type="topping", price=0.5):
            self.name = name
            self.type = type
            self.price = price

        def get_name(self):
            return self.name

        def get_type(self):
            return self.type

        def get_price(self):
            return self.price

    return MockIngredient

@pytest.fixture
def burger(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient())
    return burger

@pytest.fixture
def burger_with_ingredients(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient(name="Lettuce"))
    burger.add_ingredient(mock_ingredient(name="Tomato"))
    burger.add_ingredient(mock_ingredient(name="Cheese"))
    return burger


@pytest.fixture
def database():
    return Database()


@pytest.fixture
def ingredient():
    return Ingredient("filling", "Tomato", 0.75)

@pytest.fixture
def sauce():
    return Ingredient("sauce", "Ketchup", 1.0)



