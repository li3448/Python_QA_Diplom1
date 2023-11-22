import pytest
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.bun import Bun
from unittest.mock import Mock

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun_mock():
    return Mock(spec=Bun)

@pytest.fixture
def ingredient_mock():
    return Mock(spec=Ingredient)