import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from praktikum.burger import Burger


@pytest.fixture(scope='function')
def bun():
    bun = Bun('Крейзи_Булка', 999)
    return bun


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger


@pytest.fixture(scope='function')
def ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Крейзи_соус", 555)
    return ingredient
